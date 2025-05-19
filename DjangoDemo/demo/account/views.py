from django.shortcuts import render,redirect
from .forms import  *
from django.views import View
# Create your views here.
class Signup(View):
    def post(self,request):
        form=RegistrationForm(data=request.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('/accounts/login')
