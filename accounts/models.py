from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    Roll_CHOICE = (
        ("ADMIN", "Admin"),
        ("MANAGER", "Manager"),
        ("EMPLOYEE", "Employee"),
    )

    role = models.CharField(
        max_length=20, 
        choices=Roll_CHOICE, 
        default="EMPLOYEE"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.username
