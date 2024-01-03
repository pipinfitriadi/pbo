class Buku:
    def __init__(self, judul, penulis, harga):
        self.judul = judul
        self.penulis = penulis
        self.harga = harga

    def tampilkan_info(self):
        print(f"Informasi Buku:\nJudul: {self.judul}\nPenulis: {self.penulis}\nHarga: {self.harga}")

# menjalankan fungsi clas buku
buku_saya = Buku("Judul Buku Saya", "Penulis Saya", 100000)
buku_saya.tampilkan_info()

# daftar buku yang ada
buku1 = Buku("Judul Buku 1", "Penulis 1", 75000)
buku2 = Buku("Judul Buku 2", "Penulis 2", 90000)
buku3 = Buku("Judul Buku 3", "Penulis 3", 120000)

#menampilkan list buku yang ada
buku1.tampilkan_info()
buku2.tampilkan_info()
buku3.tampilkan_info()