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
    path('accounts/signup', views.sign_up, name="signup"),
    # Change Password
    url(r'^accounts/password_change/$', auth_views.password_change,
        {'template_name': 'myapp/registration/password_change_form.html',
         'post_change_redirect': '/accounts/password_change/done/'},
        name='password_change'),
    url(r'^accounts/password_change/done/$', auth_views.password_change_done,
        {'template_name': 'myapp/registration/password_change_done.html'},
        name='password_change_done'),
    # Reset Password
    path('accounts/password_reset/', auth_views.password_reset,
         {'template_name': 'accounts/registration/password_reset_form.html'},
         name='password_reset'),
    url(r'^accounts/password_reset/done/$', auth_views.password_reset_done,
        {'template_name': 'accounts/registration/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^accounts/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'accounts/registration/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^accounts/reset/done/$', auth_views.password_reset_complete,
        {'template_name': 'accounts/registration/password_reset_complete.html'},
        name='password_reset_complete'),
]
