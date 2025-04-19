from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager


class CustomUser(AbstractUser):
    """
    Custom user class for addional fields in the user model
    """

    objects = CustomUserManager()

    def __str__(self):
        return f"{self.username}"
