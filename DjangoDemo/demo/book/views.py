from django.shortcuts import render,redirect
from .models import Book2,Catagory2
from django.http import HttpResponse
import os
from django.conf import settings
# Create your views here.

def book_show(request,id):
    context={'book':Book2.get_by_id(id)}
    return render(request,'book/details.html',context)
def book_list(request):
    context={'books':Book2.getall()}
    return render(request,'book/list.html',context)
def book_new(request):
    context={'catagories':Catagory2.getall()}
    if(request.method=='POST'):
        #validate data
        if request.POST['Bname'] and request.POST['Bpdate'] and  request.FILES['Bimage'] and request.POST['bcat'] :
            #add new book clean code
            Book2.Add(request.POST['Bname'],request.POST['Bpdate'],request.FILES['Bimage'],request.POST['bcat'])
            return Book2.go_to_Book_List()
        else:
            context['errormsg']='Invalid data'
    return render(request, 'book/new.html',context)
def book_update(req,id):
    context={'bookobj':Book2.get_by_id(id),
             'catagories':Catagory2.getall()}
    if req.method=='POST':
        # validate data
        if req.POST['Bname'] and req.POST['Bpdate'] and req.POST['bcat']:

            # #update
            Book2.update(id,req.POST['Bname'],req.POST['Bpdate'])

            return Book2.go_to_Book_List()
        else:
            context['errormsg']='Invalid data'

    return render(req,'book/update.html',context)

def book_delete(req,id):
    return HttpResponse(f'<h1>Book deleted {id}</h1>')