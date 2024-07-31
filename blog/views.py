from django.shortcuts import render
from .models import Posts

posts = Posts.objects.all()

def home(request):
     context={
          'posts': posts
          }
     return render(request, 'blog/home.html', context)
