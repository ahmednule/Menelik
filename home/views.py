from django.shortcuts import render


schedule = [
    {
        'day': 'Mon',
        'streets': ['Gallana Rd', 'BrookSide']
    },
    {
        'day': 'Tue',
        'streets': ['Cotton Av', 'Chaka Rd']
    },
    {
        'day': 'Wed',
        'streets': ['Dennis Pritt Rd', 'Ngong Road']
    },
    {
        'day': 'Thur',
        'streets': ['Kikambala Rd', 'Ring Rd']
    },
    {
        'day': 'Fri',
        'streets': ['Menelik Rd', 'Kirichwa Rd']
    },
    {
        'day': 'Sat',
        'streets': ['Airwings Kodhek Rd', 'Ndemi Rd']
    }
]




def home(request):
    return render(request, 'home/index.html')

def contact(request):
    return render(request, 'home/contact.html')

def collection(request):
    context = {
        "week_schedule": schedule
    }
    return render(request, 'home/collection.html', context)

def recycle(request):
    return render(request, 'home/recycle.html')

def complain(request):
    return render(request, 'home/complain.html')

def about(request):
    return render(request, 'home/about.html')