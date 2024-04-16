from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.validators import RegexValidator

class NumericalPhoneField(forms.CharField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Adding a regex validator to allow only numerical input
        self.validators.append(RegexValidator(r'^\d+$', 'Please enter a valid phone number.'))


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), )
    first_name = forms.CharField(label="First Name", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    # phone = forms.CharField(label="", max_length=15,
                                # widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}))
    phone = NumericalPhoneField(label='Phone no', max_length=15,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}))
    
    # password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'password'}))

    password1 = forms.CharField(label='Password', max_length=40, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',}))
    password2 = forms.CharField(label='Confirm Password', max_length=40, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password')



