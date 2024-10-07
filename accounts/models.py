from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField()
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'password']

    objects = UserManager()
