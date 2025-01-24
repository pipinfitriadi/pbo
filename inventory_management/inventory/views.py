# inventory/views.py
from django.shortcuts import render, redirect
from .models import Product, Supplier, Order
from .forms import ProductForm, OrderForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'inventory/product_list.html', {'products': products})

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})

def order_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product
            order.save()
            return redirect('product_list')
    else:
        form = OrderForm()
    return render(request, 'inventory/order_product.html', {'form': form, 'product': product})
# inventory/views.py (tambahkan view untuk pemasok)
def supplier_orders(request):
    orders = Order.objects.filter(status='Pending')  # Menampilkan pesanan yang belum diproses
    return render(request, 'inventory/supplier_orders.html', {'orders': orders})

def update_order_status(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = request.POST.get('status')
        order.save()
        return redirect('supplier_orders')
    return render(request, 'inventory/update_order_status.html', {'order': order})
# inventory/views.py
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group

@login_required
def product_list(request):
    if request.user.groups.filter(name='Manager').exists():
        products = Product.objects.all()
        low_stock_products = products.filter(stock__lt=5)
        return render(request, 'inventory/product_list.html', {'products': products, 'low_stock_products': low_stock_products})
    else:
        return redirect('supplier_orders')

@login_required
def supplier_orders(request):
    if request.user.groups.filter(name='Supplier').exists():
        orders = Order.objects.filter(status='Pending')
        return render(request, 'inventory/supplier_orders.html', {'orders': orders})
    else:
        return redirect('product_list')