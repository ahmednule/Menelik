from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home_page"),
     path('', views.contact, name="contact_page"),
]