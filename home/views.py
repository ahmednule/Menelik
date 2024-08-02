from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from .forms import TrashCollectionForm



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
    success_message = ''
    if request.method == 'POST':
        form = TrashCollectionForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            print(f'{first_name} {last_name} \n {email} {phone}')

            success_message = 'Your Request Was submitted Successfully'
            
            # Save or handle the form data as needed
            # e.g. save to database or send a confirmation email
            context = {
                "week_schedule": schedule,
                'form': form,
                success_message: success_message
            }
            return render(request, 'home/collection.html', context)
    else:
        form = TrashCollectionForm()
    
    context = {
        "week_schedule": schedule,
        'form': form,
        success_message: success_message
    }
    return render(request, 'home/collection.html', context)

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


def contact(request):
    return render(request, 'home/contact.html' )

def  developer_compliance(request):
    return render(request, 'home/developer_compliance.html')