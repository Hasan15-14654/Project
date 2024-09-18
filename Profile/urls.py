from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Profile, name='profile'),
    path('edit/', views.EditProfile, name='editprofile')

]
