from django.urls import path
from . import views

urlpatterns = [
    path('aa', views.registerView.as_view(), name="test"),
]