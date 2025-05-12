from django.shortcuts import render
from .models import Book2
from django.http import HttpResponse
# Create your views here.
def book_list(request):

    return render(request,'book/list.html')
def book_new(request):
    return HttpResponse('<h1>New Book</h1>')
def book_update(req,id):
    return HttpResponse(f'<h1>Book updated {id}</h1>')
def book_delete(req,id):
    return HttpResponse(f'<h1>Book deleted {id}</h1>')