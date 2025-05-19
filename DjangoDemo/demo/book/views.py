from django.shortcuts import render,redirect
from .models import Book2,Catagory2
from django.http import HttpResponse
from .forms import BookForm,BookFormModel
import os
from django.conf import settings
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,UpdateView,CreateView



class Book_updateG(UpdateView):
    model = Book2
    template_name = 'book/updateform.html'
    context_object_name = 'bookobj'
    queryset = Book2.getall()
    fields = '__all__'
    # def get_form(self, form_class=None):
    #     form = super().get_form(form_class)
    #     # Filter the author queryset
    #     form.fields['catagory'].queryset =Catagory2.objects.all()
    #     return form
class Book_list_classG(ListView):
    template_name = 'book/list.html'
    model = Book2
    context_object_name = 'books'
class Book_newG(CreateView):
    model = Book2
    fields = '__all__'
    exclude=['status']
    template_name = 'book/newform.html'
    context_object_name = 'books'
    queryset = Book2.getall()

# Create your views here.

class book_list_class(View):
    def get(self,request):
        context = {'books': Book2.getall()}
        return render(request, 'book/list.html', context)

class book_deleteclass(View):
    def get(self,request,id):
        Book2.softdelete(id)
        return Book2.go_to_Book_List()
class Book_update(View):
    def get(self,request,id):
        context = {'form': BookFormModel(instance=Book2.get_by_id(id))}
        return render(request, 'book/updateform.html', context)
    def post(self,request,id):
        context={}
        form = BookFormModel(data=request.POST, files=request.FILES, instance=Book2.get_by_id(id))
        if form.is_bound and form.is_valid():
            form.save()
            return redirect('Blist')
        else:
            context['form'] = form
            context['msg'] = form.errors

        return render(request, 'book/updateform.html', context)

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
@login_required()
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
