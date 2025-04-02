from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    return render(request,"login.html")

def register(request):
    if request.method == "POST":
        id=request.POST.get("id",None)
        username=request.POST.get("username",None)
        email=request.POST.get("email",None)
        password=request.POST.get("password",None)
        confirm_password=request.POST.get("confirm-password",None)
        print(username,"username")
        print(email,"email")
        print(password,"password")
        print(confirm_password,"confirm_password")
        
        if not id:
            password_Data=''
            if password == confirm_password:
                password_Data=make_password(password)
            else:
                password=None
            password
         
            User.objects.create(username=username,email=email,password=password_Data)
            return HttpResponseRedirect('/')
        else:
            return JsonResponse({'status':"failed"})
    else:
        return render(request,"register.html")

