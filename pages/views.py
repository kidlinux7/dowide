from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, UserRegistrationForm
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *
from .forms import *
import json


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = HouseForm(request.POST or None)
            if form.is_valid():
                houseform = form.save(commit=False)
                houseform.save()
                messages.info(request,'Saved successfully')
                form = HouseForm()
                context = {'form':form}
                return redirect('home')
                
        else:
            form = HouseForm()
        context = {'form':form}
    else:
        return redirect('login')
    return render(request,"home.html",context)