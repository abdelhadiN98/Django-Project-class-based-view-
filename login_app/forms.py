
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Employee

class NewUserForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	


	class Meta:
		model = Employee
		fields = ('email','first_name','last_name','password1','password2')

class LoginForm(UserCreationForm):
	email = forms.EmailField()
	

	class Meta:
		model = Employee
		fields = ('email',)