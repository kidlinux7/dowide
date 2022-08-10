from django import forms
from .models import *


class UserForm(forms.ModelForm):
    class Meta:
    	model = User
    	fields = ['email', 'password']
    
class UserRegistrationForm(forms.ModelForm):
    class Meta:
    	model = User
    	fields = [
    		    'first_name', 
    		    'password', 
    		    'email', 
    	] 

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['owners_name','owners_phone_1','owners_phone_2','house_owner','number_of_rooms','price_per_day','minimum_booking_per_day','instructions','description','region','district','street_name','house_number','google_map','amenities']