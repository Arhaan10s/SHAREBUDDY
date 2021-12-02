from django.contrib import messages

from django.db.utils import IntegrityError
from django.shortcuts import render
from django.contrib.auth import login,logout,authenticate
from django.urls import reverse

from django.http import HttpResponse,HttpResponseRedirect

from .models import User
from .models import *
from django import forms

def home(request):
    return render(request,"templates/home.html")

def login_view(request):
     if request.method=='POST':
         username = request.POST['username']
         password = request.POST['password']
         user = authenticate(request,username=username,password=password)
         
         if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
            
         else:
            return render(request, "templates/login.html", {
                "message": "Invalid username and/or password."
            })
     else:
         return render(request, "templates/login.html")  
         
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

def register(request):
    if request.method=='POST':
        username = request.POST['username']
        email = request.POST['email']

        password = request.POST['password']
        confirmation = request.POST['confirmation']
        if password != confirmation:
            return render(request,"templates/register.html",{
                "message":"Incorrect password"
            })

        try:
            user = User.objects.create_user(username, email, password)
            user.save() 
        except IntegrityError:
            return render(request,"templates/register.html",{
                "message":"Username already taken"
            })
        login(request, user)
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request,"templates/register.html")



Abhay
