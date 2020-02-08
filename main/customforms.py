from django.forms import ModelForm
from .models import ToDo
from django import forms

class ToDoForm(ModelForm):
    class Meta:
        model = ToDo
        fields = [
            'username','label','category','details'
        ]
        widgets = {
            'username':forms.HiddenInput()
        }