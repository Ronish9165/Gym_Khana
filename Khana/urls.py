from django.contrib import admin
from django.urls import path
from Khana import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="home"),
    path("login/", views.login, name='login'),
    path("register/", views.register, name='register'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    # path("homepage/",views.homepage, name='homepage'),

    path('password_reset/',
         auth_views.PasswordResetView.as_view(
             template_name='password_reset_form.html'),
         name='password_reset'),

    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='password_reset_complete.html'),
         name='password_reset_complete'),
]