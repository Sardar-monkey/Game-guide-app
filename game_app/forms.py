from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GamePost

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class GamePostForm(forms.ModelForm):
    class Meta:
        model = GamePost
        fields = ['title', 'category', 'image', 'description']