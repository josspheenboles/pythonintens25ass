from django.shortcuts import render
from .models import Book2,Catagory2
from django.http import HttpResponse
# Create your views here.
def book_list(request):

    return render(request,'book/list.html')
def book_new(request):
    catagories=Catagory2.objects.all()
    context={}
    context['catagories']=catagories
    if(request.method=='POST'):
        #validate data

        #create object of book model
    return render(request, 'book/new.html',context)
def book_update(req,id):
    return HttpResponse(f'<h1>Book updated {id}</h1>')
def book_delete(req,id):
    return HttpResponse(f'<h1>Book deleted {id}</h1>')