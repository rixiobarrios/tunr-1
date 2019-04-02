from django.urls import path
from django.conf.urls import include
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views


urlpatterns = [
    # Login / Log Out
    path('accounts/login/', auth_views.login,
         {'template_name': 'accounts/registration/login.html'}, name='login'),
    path('accounts/logout/', auth_views.logout,
         {'template_name': 'accounts/registration/logged_out.html'}, name='logout'),
    # Sign Up
    path('accounts/signup', views.sign_up, name="signup")
]
