from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.home, name="blog_home"),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
