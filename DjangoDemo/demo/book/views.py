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
        if request.POST['Bname'] and request.POST['Bpdate'] and  request.FILES['Bimage'] and request.POST['bcat'] :
            #get selected Catagory Object
            catagoryobj=Catagory2.get_catagory_by_id(request.POST['bcat'])
            #create object of book model
            Book2.objects.create(name=request.POST['bname'],
                                 publish_date= request.POST['Bpdate'],
                                 image=request.FILES['Bimage'],
                                 catagory=request.POST['bcat'])



        else:
            context['errormsg']='Invalid data'
    return render(request, 'book/new.html',context)
def book_update(req,id):
    return HttpResponse(f'<h1>Book updated {id}</h1>')
def book_delete(req,id):
    return HttpResponse(f'<h1>Book deleted {id}</h1>')