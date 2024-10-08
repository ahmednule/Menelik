from django.urls import path
from . import views

urlpatterns = [
     path('', views.home, name="home_page"),
     path('contact/', views.contact, name="contact"),
     path('collection/', views.collection, name="collection_resident"),
     path('about/', views.about, name='about_page'),
     path('complain/', views.complain, name='complain_page'),
     path('planningact/', views.planningact, name='planningact'),
     path('legalaction/', views.legalaction, name='legalaction'),
     path('nappyrecycling/', views.nappyrecycling, name='nappyrecycling'),
     path('architects/', views.architects, name='architects'),
     path('compliance/', views.developer_compliance, name='developer_compliance'),


]