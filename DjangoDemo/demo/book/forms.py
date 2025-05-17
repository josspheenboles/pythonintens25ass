from django import forms
from django.core.validators import FileExtensionValidator
from .models import Catagory2


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