from django.shortcuts import render,redirect
from .models import Book2,Catagory2
from django.http import HttpResponse
from .forms import BookForm,BookFormModel
import os
from django.conf import settings
from django.views import View
# Create your views here.
class Book_New(View):
    context ={}
    def get(self,request):
        Book_New.context = {'form': BookForm()}
        return render(request, 'book/newform.html', Book_New.context)
    def post(self,request):

        form = BookForm(data=request.POST, files=request.FILES)
        if (form.is_bound and form.is_valid()):
            Book2.Add(form.cleaned_data['name'],
                      pdate=form.cleaned_data['publishdate'],
                      image=form.cleaned_data['image'],
                      catagoryid=form.cleaned_data['catagory'])
            return redirect('Blist')
        else:
            Book_New.context['msg'] = form.errors
        return render(request, 'book/newform.html', Book_New.context)

def book_show(request,id):
    context={'book':Book2.get_by_id(id)}
    return render(request,'book/details.html',context)
def book_list(request):
    context={'books':Book2.getall()}
    return render(request,'book/list.html',context)

def book_newformmodel(request):
    context={'form':BookFormModel}
    if(request.method=='POST'):
        form=BookFormModel(data=request.POST,files=request.FILES)
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('Blist')
        else:
            context['msg']=form.errors
            context['form']=form

    return render(request, 'book/newform.html', context)
def book_newform(request):
    context={'form':BookForm()}
    if request.method=='POST':
        form=BookForm(data=request.POST,files=request.FILES)
        if(form.is_bound and form.is_valid()):
            Book2.Add(form.cleaned_data['name'],
                      pdate=form.cleaned_data['publishdate'],
                      image=form.cleaned_data   ['image'],
                      catagoryid=form.cleaned_data['catagory'])
            return redirect('Blist')
        else:
            context['msg']=form.errors
    return render(request, 'book/newform.html', context)
def book_updateform(request,id):
    oldbookobj=Book2.get_by_id(id)
    initail_data={
        'name': oldbookobj.name,
        'publishdate': oldbookobj.publish_date,
        'image':oldbookobj.image,
        'catagory':oldbookobj.catagory.id
    }
    context={'form':BookForm(initial=initail_data)}
    if request.method=='POST':
        form=BookForm(data=request.POST,files=request.FILES,initial=initail_data)
        if form.is_bound and form.is_valid():
            oldbookobj.name=form.cleaned_data['name']
            oldbookobj.publish_date=form.cleaned_data['publishdate']
            oldbookobj.image=  form.cleaned_data['image']
            oldbookobj.catagory=Catagory2.get_catagory_by_id(  form.cleaned_data['catagory'])
            oldbookobj.save()
            return redirect('Blist')
        else:
            context['msg']=form.errors
    return render(request, 'book/updateform.html', context)
def book_updateformmodel(request,id):
    context={'form':BookFormModel(instance=Book2.get_by_id(id))}
    if request.method=='POST':
        form=BookFormModel(data=request.POST,files=request.FILES,instance=Book2.get_by_id(id))
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('Blist')
        else:
            context['form']=form
            context['msg']=form.errors

    return render(request, 'book/updateform.html', context)
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
    # Book2.harddel(id)
    Book2.softdelete(id)
    return Book2.go_to_Book_List()
