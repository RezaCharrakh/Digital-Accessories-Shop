from django import forms
from .models import User


class UserSignup(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserSignin(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
        