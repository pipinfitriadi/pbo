from inventory.views import product_list, add_product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', product_list, name='product_list'),
    path('products/add/', add_product, name='add_product'),
]