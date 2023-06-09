from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(max_length=127, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    password = models.CharField(max_length=127)
    is_seller = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
