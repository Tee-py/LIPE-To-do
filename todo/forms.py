from django import forms
from .models import DailyTodo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class TodoCreationForm(forms.ModelForm):
    class Meta:
        model = DailyTodo
        fields = ('Title',)

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}), max_length=30, required=False)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email (e.g sc_mofeloluwa@agbaDev.com)'}),
        max_length=254, required=True)
    password1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password', 'type': 'password'}), max_length=30, required=False)
    password2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'password again', 'type': 'password'}), max_length=30, required=False)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

