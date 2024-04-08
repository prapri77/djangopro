from django.urls import path
from .views import demo
from django.conf.urls.static import static



urlpatterns = [
    path('', demo),
]
