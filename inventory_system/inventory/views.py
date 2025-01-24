from django.shortcuts import redirect
from .forms import ProductForm

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'inventory/add_product.html', {'form': form})
from .models import Order

def order_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        order = Order(product=product, quantity=quantity)
        order.save()
        return redirect('product_list')
    return render(request, 'inventory/order_product.html', {'product': product})