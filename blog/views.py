from django.shortcuts import render

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
