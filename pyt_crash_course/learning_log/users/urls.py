from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    path('login/', login, name='login'),
]