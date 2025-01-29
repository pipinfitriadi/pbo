from django.urls import path
from . import views

# define a list urls pattern
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about, name='about'),
]
