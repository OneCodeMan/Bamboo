from django.db import models
from django.contrib.auth.models import User

class Deck(models.Model):
	owner = models.ForeignKey(User, null=True, default=True, related_name='o')
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=200, default='N/A')

	def __str__(self):
		return self.name 

	def get_absolute_url(self):
		return reverse('card:deck_list')

class Card(models.Model):
	owner = models.ForeignKey(User, null=True, default=True, related_name='oc')
	term = models.CharField(max_length=100, default='N/A')
	definition = models.TextField(default='N/A')
	deck = models.ForeignKey(Deck, on_delete=models.CASCADE)

	def __str__(self):
		return self.term

	def get_absolute_url(self):
		return reverse('card:deck_list')