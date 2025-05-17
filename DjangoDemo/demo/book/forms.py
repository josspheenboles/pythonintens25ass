from django import forms

class BookForm(forms.Form):
    name=forms.CharField(required=True,max_length=100,
                         widget=forms.TextInput(attrs={'style':'color:red'}),
                         )