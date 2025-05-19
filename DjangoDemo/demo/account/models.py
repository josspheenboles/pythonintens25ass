from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.
class CustomUser(AbstractBaseUser):
    # Add custom fields
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
