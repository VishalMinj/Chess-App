from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
import secrets
import string


class CustomUser(AbstractUser):
    """
    Custom user class for addional fields in the user model
    """

    def generate_private_code():
        return "".join(
            secrets.choice(string.ascii_uppercase + string.digits) for _ in range(8)
        )

    objects = CustomUserManager()
    id = models.CharField(
        primary_key=True,
        max_length=8,
        unique=True,
        editable=False,
        default=generate_private_code,
    )

    def __str__(self):
        return f"{self.username}"
