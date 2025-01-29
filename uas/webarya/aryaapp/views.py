from django.shortcuts import render, redirect
from .models import karyaSeni

# Create your views here.

def home_view(request):
    products = karyaSeni.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})