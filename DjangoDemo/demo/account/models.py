from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Account(AbstractUser):
    bio = models.TextField(blank=True)
    birth_date = models.DateField(null=True, blank=True)
