from django.urls import path
from .views import index

# define a list urls pattern
urlpatterns = [
    path("", index, name= "index"),
]
