"""Purauth models module."""
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """Custom user."""

    email = models.EmailField(unique=True)
    is_premium = models.BooleanField("premium status", default=False)
