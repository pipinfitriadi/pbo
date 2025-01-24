from django.shortcuts import render
from .models import karyaSeni

# Create your views here.
def index(request):
    karya = karyaSeni.objects.all()
    konteks = {'karya': karya}
    return render(request, 'index.html', konteks)
