from django.shortcuts import render, redirect
from .form import ContactForm

# Create your views here.

def home_view(request):
    return render(request, 'aryaapp/home.html')

# Define the contact_view function to handle contact form
def contact_view(request):
   if request.method == "POST":
       form = ContactForm(request.POST)
       if form.is_valid():
           form.send_email()
           return redirect('contact-success')
   else:
       form = ContactForm()
   context = {'form':form}
   return render(request, 'aryaapp/contact.html', context)

# define the contact_success_view function to handle the success page
def contact_success_view(request):
    return render(request, 'aryaapp/contact_success.html')