from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.extend),
    path('1',views.loopex),
    path('2',views.include),
    path('3',views.home,name= "home"),
    path('4',views.index,name ="index"),
    path('5',views.first),
    path('6',views.time)
    ]