from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm


def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def collection(request):
    return render(request, 'home/collection.html')

def recycle(request):
    return render(request, 'home/recycle.html')

def complain(request):
    return render(request, 'home/complain.html')

def about(request):
    return render(request, 'home/about.html')

def planningact(request):
    return render(request, 'home/planningact.html' )

def legalaction(request):
    return render(request, 'home/legalaction.html' )

def nappyrecycling(request):
    return render(request, 'home/nappyrecycling.html' )