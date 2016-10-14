from django.conf.urls import url
from . import views

app_name = 'card'

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='deck_list'),
	url(r'^(?P<deck>[0-9]+)/$', views.DeckView.as_view(), name='detail'),
	url(r'^deck/new/$', views.deck_new, name='deck_new'),
	url(r'^deck/(?P<deck>[0-9]+)/edit/$', views.deck_edit, name='deck_edit'),
	url(r'^deck/(?P<deck>[0-9]+)/delete/$', views.deck_delete, name='deck_delete'),

	url(r'^deck/(?P<deck>[0-9]+)/new/$', views.card_new, name='card_new'),
	url(r'^deck/(?P<deck>[0-9]+)/card/(?P<card>[0-9]+)/$', views.card_delete, name='card_delete'),

	url(r'^register/$', views.UserFormView.as_view(), name='register'),
	url(r'^about/$', views.AboutView.as_view(), name='about'),
	url(r'^login/$', views.LoginView.as_view(), name='login'),
	url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]