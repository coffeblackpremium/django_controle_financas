from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def login(request):
    pass
