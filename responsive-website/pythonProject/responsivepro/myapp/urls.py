from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from .views import demo, register,custom_login,custom_logout,success
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    path('', demo),
    path('blogapp/', include('blogapp.urls')),
    path('register', register, name="register"),
    path('login', custom_login, name='login'),
    path('logout', custom_logout, name='logout'),
    # path('login', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('success', success, name="success")


]