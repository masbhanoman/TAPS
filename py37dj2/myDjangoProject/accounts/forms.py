#good resource
#http://kevindias.com/writing/django-class-based-views-multiple-inline-formsets/

from django.forms import ModelForm
from .models import Order

#we can do classbased form too, but modelform is better n easy

from django.contrib.auth.forms import UserCreationForm 
from django import forms
from django.contrib.auth.models import User #django User model
#we are enhancing a django-pre-build model for our use
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2',]

class OrderForm(ModelForm): 
	class Meta: 
		model = Order
		fields = '__all__' #['customer', 'product']