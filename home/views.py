from django.shortcuts import render

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