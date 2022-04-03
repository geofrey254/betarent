from django.forms import ModelForm, Textarea, FileInput, DateTimeField, TextInput
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import List, ListImage
class CreateUserForm(UserCreationForm):
    class Meta:
        model   =   User
        fields  =   ['username', 'email', 'first_name', 'last_name', 'password1','password2']
