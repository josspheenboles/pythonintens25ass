from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['password','username']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields='__all__'
        exclude=['last_login','date_joined','is_superuser','is_active','groups','user_permissions']