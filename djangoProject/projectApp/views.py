from django.shortcuts import render
from json import dumps
from django.views.generic import ListView, TemplateView, CreateView
from .models import UserModel
from .forms import UserSignup
from django.urls import reverse_lazy


class registerView(CreateView):
    model = UserModel
    form_class = UserSignup
    template_name = 'test.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user_username = form.cleaned_data.get('username')
        user_email = form.cleaned_data.get('email')
        user_password = form.cleaned_data.get('password')
        is_exist_email = UserModel.objects.filter(email__iexact=user_email).exists()
        if is_exist_email:
            form.add_error('email', 'Email already registered')
            return self.form_invalid(form)
        else:
            new_user = form.save(commit=False)
            new_user.username = user_username
            new_user.email = user_email
            new_user.set_password(user_password)
            new_user.save()
            response = super().form_valid(form)
            return response
