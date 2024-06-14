from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm



class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserSignin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class Register(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']  # Add other necessary fields


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
