from django import forms
from .models import Card, Deck
from django.contrib.auth.models import User

class DeckForm(forms.ModelForm):

	class Meta:
		model = Deck 
		fields = ('name', 'description')

class CardForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		# Pop() removes 'user' from the kwargs dictionary and populates the user variable
		user = kwargs.pop('owner') 
		super(CardForm, self).__init__(*args, **kwargs)
		self.fields['deck'] = forms.ModelChoiceField( # modify choices on 'deck' field
			queryset=Deck.objects.filter(owner=user)
		)

	class Meta:
		model = Card 
		fields = ('term', 'definition', 'deck')

class SignUpForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username', 'first_name', 'last_name', 'password']

class LogInForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User 
		fields = ['username', 'password']