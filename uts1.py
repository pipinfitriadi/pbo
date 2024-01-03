class Buku:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga

    def informasibuku(self):
        print("====Informasi Buku====")
        print("Judul Buku : ", self.judul)
        print("Penulis Buku : ", self.penulis)
        print("Harga Buku : ", self.harga)


Mybook = Buku("Harry Potter", "J.K. Rowling", 150000)
Mybook.informasibuku()
