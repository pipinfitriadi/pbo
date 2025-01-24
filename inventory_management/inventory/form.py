# inventory/forms.py
from django import forms
from .models import Product, Order

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'supplier']

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']