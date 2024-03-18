from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('index/', views.index),
    path('name', views.nameview),
    path('cond/', views.check_age),

]