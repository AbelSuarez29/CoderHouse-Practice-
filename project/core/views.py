from django.shortcuts import render, redirect
from django.contrib.auth import logout 

def home(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def exit(request):
    logout(request)
    return redirect("core:index")