# inventory_management/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),  # Mengarahkan ke URL aplikasi inventory
]
# inventory/urls.py
from django.urls import path
from .views import product_list, add_product, order_product

urlpatterns = [
    path('', product_list, name='product_list'),
    path('add/', add_product, name='add_product'),
    path('order/<int:product_id>/', order_product, name='order_product'),
]
# inventory/urls.py (tambahkan URL untuk pemasok)
urlpatterns += [
    path('supplier/orders/', supplier_orders, name='supplier_orders'),
    path('supplier/orders/update/<int:order_id>/', update_order_status, name='update_order_status'),
]
# inventory_management/urls.py
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]