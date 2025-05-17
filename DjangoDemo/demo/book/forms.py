from django import forms
from django.core.validators import FileExtensionValidator
from .models import *

class BookFormModel(forms.ModelForm):
    class Meta:
        model=Book2
        fields='__all__'
        exculde=['status','Name']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['image'].widget.attrs.update({'accept': 'image/*'})
        self.fields['publish_date'].widget=forms.DateInput(attrs={'type':'date'})



class BookForm(forms.Form):
    name=forms.CharField(required=True,max_length=100,
                         widget=forms.TextInput(attrs={'style':'color:red'}),
                         )
    publishdate=forms.DateField(label='Publish Date',
                                widget=forms.DateInput(attrs={'type':'date'}))

    image=forms.ImageField(label='Book Cover',validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])
    ],
   widget=forms.FileInput(attrs={'accept':'image/jpeg, image/png'})
                           )

    catagory=forms.ChoiceField(choices=((catagory.id,catagory.name) for catagory in Catagory2.getall()))