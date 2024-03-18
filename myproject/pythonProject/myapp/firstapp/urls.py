from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='firstapp'),
    path('login/',views.login, name='firstapp'),
    path('contact/',views.contact, name='firstapp'),

]



