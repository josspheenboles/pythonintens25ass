from django import forms
from .models import *

class LoginForm(forms.Form):
    username=forms.CharField(max_length=123)
    password=forms.CharField(widget=forms.PasswordInput())
    # class Meta:
    #     model = CustomUser
        # fields = ['username','password']


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields='__all__'
        exclude=['last_login','date_joined','is_superuser','is_active','groups','user_permissions']