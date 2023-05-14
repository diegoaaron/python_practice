from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.MyLoginView.as_view(template_name='users/login.html'), name = 'login'),
    path('logout/', views.logout_view, name = 'logout'),
]