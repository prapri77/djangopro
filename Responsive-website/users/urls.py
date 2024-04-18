from django.urls import path


from . import views


urlpatterns = [
    #path("register/", views.SignUp.as_view(), name="register"),
    path('register/', views.register, name='register'),
    path('login/', views.c_login, name='login'),
    path('success', views.success, name='success'),
    path('registration_success/',views.registration_success, name='registration_success'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('logout/', views.c_logout, name='logout'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
    # path('change_password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
 ]

