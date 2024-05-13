from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    username = None
    
    email = models.EmailField(_("email address"), unique=True)

    first_name = models.CharField(max_length=150)

    last_name = models.CharField(max_length=150)

    # phone = models.CharField(max_length=15, default='',)
    password = models.CharField(max_length=128)

    phone = models.CharField(max_length=10,unique=True, blank=True, null=True, validators=[RegexValidator(
    regex=r"^\d{10}", message="Phone number must be 10 digits only.")])
    address = models.TextField(max_length=50, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    otp = models.CharField(max_length=6, null=True, blank=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)
    max_otp_try = models.CharField(max_length=2, default=3)
    otp_max_out = models.DateTimeField(blank=True, null=True)

   

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    # def get_full_name(self):
    #     return f"{self.first_name} {self.last_name}"






