from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

path('scookie', views.setcookie),
path('gcookie', views.getcookie),
path('csv', views.getfile),

    ]

