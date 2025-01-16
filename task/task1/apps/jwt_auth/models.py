from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class CustomUser(AbstractUser):
    bio=models.TextField(blank=True, null=True)

    groups = models.ManyToManyField(
        'auth.Group', 
        related_name='customuser_set',  # custom related name
        blank=True
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions',  # custom related name
        blank=True
    )