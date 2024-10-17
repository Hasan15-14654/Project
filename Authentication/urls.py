from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationView, name='registration'),
    path('verify-email/', views.VerifyEmailView, name='verify_email'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('password_change/', views.CustomPasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
]
