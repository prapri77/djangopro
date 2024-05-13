from django.urls import path

from . import views
from .views import LoginView, VerifyOTPView


urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.c_login, name='login'),
    path('success', views.success, name='success'),
    path('registration_success/',views.registration_success, name='registration_success'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.c_logout, name='logout'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    
    # VerifyOTPView
    path('login/', LoginView.as_view(), name='login'),
    path('verify-otp/', VerifyOTPView.as_view(), name='verify-otp'),

    #this for checking password before login itself
    # path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    # path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/',  CustomPasswordResetView.as_view(), name='password_reset_done'),  
    # path('reset/<uidb64>/<token>/',  CustomPasswordResetView.as_view(), name='password_reset_confirm'),  
    # path('reset/done/', CustomPasswordResetView.as_view(), name='password_reset_success'),  
]

