from datetime import date

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

from subscriptions.models import Subscriptions


class NewUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    user_name = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    is_active = models.BooleanField(default=True)
    sub = models.ForeignKey(Subscriptions, default=1, on_delete=models.CASCADE)
    creation_date = models.DateField(default=date.today)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name', 'password']

    objects = UserManager()

# Create your models here.
