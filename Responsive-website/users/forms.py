from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator, MinLengthValidator, MaxLengthValidator

# class NumericalPhoneField(forms.CharField):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         # Adding a regex validator to allow only numerical input
#         self.validators.append(RegexValidator(r'^\d+$', 'Please enter a valid phone number.'))
#         MinLengthValidator(10),
#         MaxLengthValidator(15),

# this is for registration
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}), )
    first_name = forms.CharField(label="First Name", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="Last Name", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    phone = forms.CharField(validators=[MinLengthValidator(10), MaxLengthValidator(10),
                                        RegexValidator(r'^[0-9]*$', 'Only numerical values are allowed.')],
                                          label="Phone no", max_length=15,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'phone'}))
    
    password1 = forms.CharField(label='Password', max_length=40, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',}))
    password2 = forms.CharField(label='Confirm Password', max_length=40, widget=forms.TextInput(attrs={'type': 'text', 'class': 'form-control',}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if CustomUser.objects.filter(phone=phone).exists():
            raise forms.ValidationError("This phone number is already registered.")
        return phone


class CustomUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget = forms.HiddenInput()
    # password = forms.CharField(label="", widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone')
       


class CustomLoginForm(forms.Form):
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'text'}))