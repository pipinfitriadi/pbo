from django.shortcuts import render, redirect
from .models import karyaSeni, Category
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

# Create your views here.

def category(request, foo):
    foo = foo.replace('-', ' ')
    # ngambil category dari url
    try:
        # melihat category
        category = Category.objects.get(name=foo)
        products = karyaSeni.objects.filter(Category=category)
        return render(request, 'category.html', {'products': products, 'category':category})

    except:
        messages.success(request, ("category tersebut tidak ada"))
        return redirect('home')

def product(request,pk):
    product = karyaSeni.objects.get(id=pk)
    return render(request, 'product.html', {'product':product})

def home_view(request):
    products = karyaSeni.objects.all()
    return render(request, 'home.html', {'products':products})

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ("You have been logged in!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect('login')
    
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("kamu telah logout"))
    return redirect ('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # log in user
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("You have been registered!"))
            return redirect('home')
        else:
            messages.success(request, ("There was an error, please try again!"))
            return redirect('register')
    else:
        return render(request, 'register.html', {'form': form})
