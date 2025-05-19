from django.db import models
from django.contrib.auth.models import AbstractUser,AbstractBaseUser
# Create your models here.
class CustomUser(AbstractUser):
    # Add custom fields
    email_confirm = models.BooleanField(default=False)