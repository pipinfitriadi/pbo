from django.urls import path
from . import views

urlpatterns = [
  path('', views.dashboard1, name='dashboard1')
]