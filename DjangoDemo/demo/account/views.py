from django.shortcuts import render,redirect
from .forms import  *
from django.views import View
from django.contrib.auth import login,logout,authenticate


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'registration/login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(data=request.POST)

        if (form.is_bound):
            obj = authenticate( request,username=request.POST['username'],password= request.POST['password'])
            if (obj is not None):
                login(request,obj)
                return redirect('Blist')
            else:
                return render(request, 'registration/login.html', {'form': form,'msg':'invlaid username & pass'})
        else:
            return render(request, 'registration/login.html', {'form': form})


class Signup(View):
    def get(self,request):
        return render(request,'registration/signup.html',{'form':RegistrationForm()})
    def post(self,request):
        form=RegistrationForm(data=request.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('/accounts/login/')
        else:

                return redirect('/accounts/login')
