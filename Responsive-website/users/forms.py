from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), )
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    phone = forms.CharField(label="", max_length=15,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}))
    
    # password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'password'}))

    password1 = forms.CharField(label='Password', widget=forms.TextInput(attrs={'type': 'text'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.TextInput(attrs={'type': 'text'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password')
