from django.forms import ModelForm
from django import forms
from .models import *

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
          'body' : forms.TextInput(attrs={'class': 'p-4 text-black', 'placeholder': 'Add message ...', 'maxlength' : '300', 'autofocus': True }),
        } 
        