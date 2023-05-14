from django.urls import path, include
import django.contrib.auth.urls
from . import views

urlpatterns = [
    path('login/', include('django.contrib.auth.urls'), name='login'),
]