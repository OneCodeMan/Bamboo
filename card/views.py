from django.shortcuts import render, redirect, get_object_or_404
from .models import Deck, Card
from django.views import generic
from django.views.generic.detail import DetailView
from .forms import DeckForm, CardForm, SignUpForm, LogInForm
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from django.contrib.auth.models import User

# list of decks
class IndexView(generic.ListView):
	template_name = 'card/deck_list.html'
	context_object_name = 'decks'

	def get_queryset(self):
		if self.request.user.is_authenticated():
			return Deck.objects.filter(owner=self.request.user)
		else:
			return None

# about page
class AboutView(TemplateView):
	template_name = 'card/about.html'

# deck stuff
class DeckView(DetailView):
	model = Deck
	pk_url_kwarg = "deck"
	template_name = 'card/deck.html'

def deck_new(request):
	if request.method == "POST":
		form = DeckForm(request.POST)
		if form.is_valid():
			deck = form.save(commit=False)
			deck.owner = request.user
			deck.save()
			return redirect('card:deck_list')
	else:
		form = DeckForm()
	return render(request, 'card/deck_edit.html', {'form': form})

def deck_edit(request, deck):
	deck = get_object_or_404(Deck, pk=deck)
	if request.method == "POST":
		form = DeckForm(request.POST, instance=deck)
		if form.is_valid():
			deck = form.save(commit=False)
			deck.save()
			return redirect('card:deck_list')
	else:
		form = DeckForm(instance=deck)
	return render(request, 'card/deck_edit.html', {'form': form})

def deck_delete(request, deck):
	deck = get_object_or_404(Deck, pk=deck)
	deck.delete()
	return redirect('card:deck_list')

# cards
def card_new(request, deck):
	if request.method == "POST":
		form = CardForm(request.POST, owner=request.user)
		if form.is_valid():
			card = form.save(commit=False)
			card.save()
			return redirect('card:detail', deck)
	else:
		form = CardForm(initial={'deck': deck}, owner=request.user) # this initial field sets card's deck as current deck
	return render(request, 'card/card_edit.html', {'form': form})

def card_delete(request, deck, card):
	card = get_object_or_404(Card, pk=card)
	card.delete()
	return redirect('card:detail', deck)

# user
class UserFormView(View):
	form_class = SignUpForm
	template_name = 'card/registration_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		if form.is_valid():
			user = form.save(commit=False)

			username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			
			if not User.objects.filter(username=username).exists():
				password = form.cleaned_data['password']
				user.set_password(password)
				user.save()

				user = authenticate(username=username, password=password)

				if user is not None:

					if user.is_active:
						login(request, user)
						return redirect('card:deck_list')
				else:
					pass
			else:
				pass

def check_username(request):
	if not request.GET.get('username'):
		return render(request, '404.html', {'message': _('You shall not pass')}, status=405)
	if User.objects.filter(username=request.GET.get('username').encode('utf-8')).count():
		return HttpResponse('user exists', content_type="text/plain")
	return HttpResponse("good user", content_type='text/plain')

class LoginView(View):
	form_class = LogInForm 
	template_name = 'card/login_form.html'

	def get(self, request):
		form = self.form_class(None)
		return render(request, self.template_name, {'form': form})

	def post(self, request):
		form = self.form_class(request.POST)

		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:

			if user.is_active:
				login(request, user)
				return redirect('card:deck_list')
			else:
				pass
		else:
			pass

class LogoutView(View):

	def get(self, request):
		logout(request)
		return redirect('card:deck_list')