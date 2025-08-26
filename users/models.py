from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Roles(models.TextChoices):
        BUYER = "buyer", "Buyer"
        SELLER = "seller", "Seller"

    role = models.CharField(max_length=10, choices=Roles.choices, default=Roles.BUYER)

    def __str__(self):
        return f"{self.username} ({self.role})"

