from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Posts
from django.contrib import messages

def home(request):
    posts = Posts.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
        else:
            messages.error(request, 'Please correct the error(s) below.')
    else:
        form = UserCreationForm()
    return render(request, 'blog/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Consider redirecting to a more specific page
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})
