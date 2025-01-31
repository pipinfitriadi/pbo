class Cart():
    def __init__(self, request):
        self.session = request.session

        # dapat kan data dari session key kalau ada
        cart = self.session.get('session_key')

        # kalau user baru, tidak ada session key, maka dibuat session key
        if 'session key' not in request.session:
            cart = self.session['session_key'] = {}
        
        # memastikan cart tersedia di semua page website
        self.cart = cart

    def add(self, product):
        product_id = str(product.id)

        # Logic to add or update the product in the cart
        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'harga': str(product.harga)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
