class Produk:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.__id_produk = id_produk  # Enkapsulasi atribut
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok

    def tampilkan_info(self):
        # Menampilkan detail produk
        return f"ID: {self.__id_produk}, Nama: {self.__nama}, Kategori: {self.__kategori}, Harga: {self.__harga}, Stok: {self.__stok}"

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def kurangi_stok(self, jumlah):
        self.__stok -= jumlah


class Transaksi:
    def __init__(self, id_transaksi, produk, jumlah):
        self.__id_transaksi = id_transaksi
        self.__produk = produk
        self.__jumlah = jumlah
        self.__total_harga = self.hitung_total_harga()

    def hitung_total_harga(self):
        # Menghitung total harga berdasarkan jumlah produk dan harga produk
        return self.__produk.get_harga() * self.__jumlah

    def tampilkan_info(self):
        # Override metode untuk menampilkan ringkasan transaksi
        return f"ID Transaksi: {self.__id_transaksi}, Produk: {self.__produk.tampilkan_info()}, Jumlah: {self.__jumlah}, Total Harga: {self.__total_harga}"


class Kasir:
    def __init__(self):
        self.produk_list = []
        self.transaksi_list = []

    def tambah_produk(self, produk):
        self.produk_list.append(produk)

    def hapus_produk(self, produk):
        self.produk_list.remove(produk)

    def proses_transaksi(self, transaksi):
        # Memproses transaksi dan mengurangi stok produk
        produk = transaksi._Transaksi__produk
        if produk.get_stok() >= transaksi._Transaksi__jumlah:
            produk.kurangi_stok(transaksi._Transaksi__jumlah)
            self.transaksi_list.append(transaksi)
            print("Transaksi berhasil diproses.")
        else:
            print("Stok tidak cukup untuk transaksi ini.")


class SistemInventaris:
    def __init__(self):
        self.kasir = Kasir()

    def tambah_produk(self, id_produk, nama, kategori, harga, stok):
        produk = Produk(id_produk, nama, kategori, harga, stok)
        self.kasir.tambah_produk(produk)

    def tampilkan_daftar_produk(self):
        for produk in self.kasir.produk_list:
            print(produk.tampilkan_info())

    def tampilkan_daftar_transaksi(self):
        for transaksi in self.kasir.transaksi_list:
            print(transaksi.tampilkan_info())


# Contoh penggunaan
if __name__ == "__main__":
    sistem = SistemInventaris()
    
    # Menambahkan produk
    sistem.tambah_produk(1, "Laptop", "Elektronik", 15000000, 10)
    sistem.tambah_produk(2, "Mouse", "Aksesoris", 50000, 50)
    
    print("Daftar Produk:")
    sistem.tampilkan_daftar_produk()

    # Proses transaksi
    produk_laptop = sistem.kasir.produk_list[0]  # Mengambil produk Laptop
    transaksi1 = Transaksi(1, produk_laptop, 2)
    sistem.kasir.proses_transaksi(transaksi1)

    print("\nDaftar Transaksi:")
    sistem.tampilkan_daftar_transaksi()

    print("\nDaftar Produk setelah transaksi:")
    sistem.tampilkan_daftar_produk()