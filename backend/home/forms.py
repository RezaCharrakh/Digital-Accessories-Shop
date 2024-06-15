from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }
#
# class UserSignup(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#
# class UserSignin(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
#
#
# class Register(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'email']  # Add other necessary fields
#
#
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
