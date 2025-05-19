from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.
class CustomUser(AbstractBaseUser):
    # Add custom fields
    username=models.CharField(max_length=20)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
