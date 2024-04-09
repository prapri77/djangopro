from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import demo


urlpatterns = [
    
    path('', demo),
    path('blogapp/', include('blogapp.urls')),
]