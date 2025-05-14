from django.shortcuts import render,redirect
from .models import Book2,Catagory2
from django.http import HttpResponse
# Create your views here.
def book_list(request):

    return render(request,'book/list.html')
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
    return HttpResponse(f'<h1>Book updated {id}</h1>')
def book_delete(req,id):
    return HttpResponse(f'<h1>Book deleted {id}</h1>')