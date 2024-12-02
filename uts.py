class Produk:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.__id_produk = id_produk  # Enkapsulasi atribut
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok

    
    def get_id_produk(self):
        return self.__id_produk

    def get_nama(self):
        return self.__nama

    def get_kategori(self):
        return self.__kategori

    def get_harga(self):
        return self.__harga

    def get_stok(self):
        return self.__stok

    def set_stok(self, stok):
        self.__stok = stok

    def kurangi_stok(self, jumlah):
        self.__stok -= jumlah

    # Menampilkan informasi produk
    def tampilkan_info(self):
        return (f"ID: {self.__id_produk}, Nama: {self.__nama}, "
                f"Kategori: {self.__kategori}, Harga: {self.__harga}, Stok: {self.__stok}")


# Kelas Transaksi
class Transaksi:
    def __init__(self, id_transaksi, produk, jumlah):
        self.__id_transaksi = id_transaksi
        self.__produk = produk
        self.__jumlah = jumlah
        self.__total_harga = self.hitung_total_harga()

    # Menghitung total harga
    def hitung_total_harga(self):
        return self.__produk.get_harga() * self.__jumlah

    # Override metode tampilkan_info() (Polimorfisme)
    def tampilkan_info(self):
        return (f"ID Transaksi: {self.__id_transaksi}, "
                f"Produk: {self.__produk.get_nama()}, "
                f"Jumlah: {self.__jumlah}, Total Harga: {self.__total_harga}")


# Kelas Kasir
class Kasir:
    def __init__(self):
        self.produk_list = []
        self.transaksi_list = []

    # Menambahkan produk ke daftar produk
    def tambah_produk(self, produk):
        self.produk_list.append(produk)

    # Menghapus produk dari daftar produk
    def hapus_produk(self, produk):
        if produk in self.produk_list:
            self.produk_list.remove(produk)

    # Memproses transaksi dan mengurangi stok produk
    def proses_transaksi(self, transaksi):
        produk = transaksi._Transaksi__produk
        if produk.get_stok() >= transaksi._Transaksi__jumlah:
            produk.kurangi_stok(transaksi._Transaksi__jumlah)
            self.transaksi_list.append(transaksi)
            print("Transaksi berhasil diproses.")
        else:
            print("Stok tidak cukup untuk transaksi ini.")


# Kelas Sistem Inventaris
class SistemInventaris:
    def __init__(self):
        self.kasir = Kasir()

    # Menambahkan produk baru ke inventaris
    def tambah_produk(self, id_produk, nama, kategori, harga, stok):
        produk = Produk(id_produk, nama, kategori, harga, stok)
        self.kasir.tambah_produk(produk)

    # Menampilkan daftar produk
    def tampilkan_daftar_produk(self):
        if not self.kasir.produk_list:
            print("Tidak ada produk dalam inventaris.")
        else:
            for produk in self.kasir.produk_list:
                print(produk.tampilkan_info())

    # Menampilkan daftar transaksi
    def tampilkan_daftar_transaksi(self):
        if not self.kasir.transaksi_list:
            print("Tidak ada transaksi yang diproses.")
        else:
            for transaksi in self.kasir.transaksi_list:
                print(transaksi.tampilkan_info())


# Contoh Penggunaan
if __name__ == "__main__":
    # Membuat sistem inventaris
    sistem = SistemInventaris()

    # Menambahkan produk
    sistem.tambah_produk(1, "Laptop", "Elektronik", 15000000, 10)
    sistem.tambah_produk(2, "Mouse", "Aksesoris", 50000, 50)

    # Menampilkan daftar produk
    print("Daftar Produk:")
    sistem.tampilkan_daftar_produk()

    # Membuat transaksi dan memprosesnya
    produk_laptop = sistem.kasir.produk_list[0]  # Mengambil produk Laptop
    transaksi1 = Transaksi(1, produk_laptop, 2)
    sistem.kasir.proses_transaksi(transaksi1)

    # Menampilkan daftar transaksi
    print("\nDaftar Transaksi:")
    sistem.tampilkan_daftar_transaksi()

    # Menampilkan daftar produk setelah transaksi
    print("\nDaftar Produk setelah transaksi:")
    sistem.tampilkan_daftar_produk()
