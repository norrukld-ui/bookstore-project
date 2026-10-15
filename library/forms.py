from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'tags', 'price', 'pages', 'published']
        widgets = {
            'published': forms.DateInput(attrs={'type': 'date'}),
        }