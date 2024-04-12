from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import demo
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', demo),
    path('blogapp/', include('blogapp.urls')),
    path('loginapp/', include('loginapp.urls')),
  
]