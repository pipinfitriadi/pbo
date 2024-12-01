class Produk:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.__id_produk = id_produk
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok

    # Metode untuk menampilkan informasi produk
    def tampilkan_info(self):
        info = f"ID: {self.__id_produk}, Nama: {self.__nama}, Kategori: {self.__kategori}, Harga: {self.__harga}, Stok: {self.__stok}"
        return info

    # Getter untuk stok
    def get_stok(self):
        return self.__stok

    # Setter untuk stok
    def set_stok(self, stok):
        self.__stok = stok

        class Transaksi:
    def _init_(self, id_transaksi, produk, jumlah):
        self.__id_transaksi = id_transaksi
        self.__produk = produk
        self.__jumlah = jumlah
        self.__total_harga = self.hitung_total_harga()

    # Metode untuk menghitung total harga
    def hitung_total_harga(self):
        return self._produk.get_harga() * self._jumlah

    # Metode untuk menampilkan ringkasan transaksi
    def tampilkan_info(self):
        info = f"ID Transaksi: {self._id_transaksi}, Produk: {self.produk.get_nama()}, Jumlah: {self.jumlah}, Total Harga: {self._total_harga}"
        return info


class Kasir:
    def _init_(self):
        self.__transaksi_list = []

    # Metode untuk menambah produk
    def tambah_produk(self, produk):
        # logika untuk menambah produk ke inventaris
        pass

    # Metode untuk menghapus produk
    def hapus_produk(self, produk):
        # logika untuk menghapus produk dari inventaris
        pass

    # Metode untuk memproses transaksi
    def proses_transaksi(self, transaksi):
        # Mengurangi stok produk
        if transaksi.get_produk().get_stok() >= transaksi.get_jumlah():
            transaksi.get_produk().set_stok(transaksi.get_produk().get_stok() - transaksi.get_jumlah())
            self.__transaksi_list.append(transaksi)
            print("Transaksi berhasil!")
        else:
            print("Stok tidak cukup!")


class SistemInventaris:
    def _init_(self):
        self.__daftar_produk = []
        self.__daftar_transaksi = []

    # Metode untuk menambah produk baru ke inventaris
    def tambah_produk(self, produk):
        self.__daftar_produk.append(produk)

    # Metode untuk menampilkan daftar produk
    def tampilkan_daftar_produk(self):
        for produk in self.__daftar_produk:
            print(produk.tampilkan_info())

    # Metode untuk menampilkan daftar transaksi
    def tampilkan_daftar_transaksi(self):
        for transaksi in self.__daftar_transaksi:
            print(transaksi.tampilkan_info())


# Contoh penggunaan
if _name_ == "_main_":
    # Membuat produk
    produk1 = Produk(1, "Buku", "Alat Tulis", 50000, 10)
    produk2 = Produk(2, "Pensil", "Alat Tulis", 2000, 50)

    # Membuat sistem inventaris
    sistem_inventaris = SistemInventaris()
    sistem_inventaris.tambah_produk(produk1)
    sistem_inventaris.tambah_produk(produk2)

    # Menampilkan produk
    print("Daftar Produk:")
    sistem_inventaris.tampilkan_daftar_produk()

    # Membuat kasir
    kasir = Kasir()

    # Proses transaksi
    transaksi1 = Transaksi(1, produk1, 2)
    kasir.proses_transaksi(transaksi1)

    # Menampilkan daftar transaksi
    print("\nDaftar Transaksi:")
    sistem_inventaris.tampilkan_daftar_transaksi()