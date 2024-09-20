from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'isbn']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

class BookFilterForm(forms.Form):
    title = forms.CharField(required=False)
    author = forms.CharField(required=False)
    genre = forms.CharField(required=False)