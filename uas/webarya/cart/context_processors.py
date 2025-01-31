from .cart import Cart

# membuat context processor sehingga cart bisaa berjalan di semua page website
def cart(request):
    #mengembalikan default data dari cart
    return {'cart': Cart(request)}
