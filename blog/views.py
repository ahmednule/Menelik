from django.shortcuts import render
from .models import Posts
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def home(request):
    return render(request, 'home/index.html')

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog:login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog:blog_home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

posts = Posts.objects.all()

def home(request):
     context={
          'posts': posts
          }
     return render(request, 'blog/home.html', context)
