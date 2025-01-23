from django.urls import path
from . import views

# define a list urls pattern
urlpatterns = [
    path("", views.index)
]
