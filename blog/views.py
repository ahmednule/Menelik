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

posts =  [

    {
        'author': 'Hilary Gee',
        'title': 'Uncontrolled Tall Buildings',
        'content': 'This is a blog post about the tall builds, which are not supposed to be around',
        'date_posted': 'August 27, 2021',

    }, 
    {
        'author': 'Jack M',
        'title': 'Environmental Polution',
        'content': 'This is a blog post about Environmental Polution',
        'date_posted': 'August 27, 2023', 
    },
    {
        'author': 'Loisa Saisa',
        'title': 'Noise Pollution',
        'content': 'This is a blog post about Noise Pollution',
        'date_posted': 'August 27, 2023', 
    },
    {
         
        'author': 'Ahmed Nule',
        'title': 'Poor Waste Management',
        'content': 'This is a blog post about poor waste management',
        'date_posted': 'August 27, 2023', 
    
    }
]

def home(request):
     context={
          'posts': posts
          }
     return render(request, 'blog/home.html', context)
