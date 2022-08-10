from django import forms
from .models import *


class AccountForm(forms.ModelForm):
    class Meta:
    	model = Account
    	fields = ['fullname', 'email','phone_number','password']
    
