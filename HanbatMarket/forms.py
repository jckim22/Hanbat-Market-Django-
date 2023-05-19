from django import forms
from django.forms import widgets
from .models import Board

class RegistForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['title', 'author', 'price','content']  # '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }