from django.shortcuts import render, redirect
from .models import karyaSeni

# Create your views here.

def home_view(request):
    products = karyaSeni.objects.all()
    return render(request, 'home.html', {'products':products})

