# inventory/admin.py
from django.contrib import admin
from .models import Supplier, Product, Order

admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Order)