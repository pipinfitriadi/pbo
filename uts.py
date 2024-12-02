# Kelas Produk
class Produk:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.__id_produk = id_produk
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok

    # Getter dan Setter untuk atribut yang dienkapsulasi
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

    # Metode untuk menampilkan informasi produk
    def tampilkan_info(self):
        print(f"ID Produk: {self.__id_produk}")
        print(f"Nama: {self.__nama}")
        print(f"Kategori: {self.__kategori}")
        print(f"Harga: {self.__harga}")
        print(f"Stok: {self.__stok}\n")


# Kelas Transaksi
class Transaksi:
    def __init__(self, id_transaksi, produk, jumlah):
        self.__id_transaksi = id_transaksi
        self.__produk = produk
        self.__jumlah = jumlah
        self.__total_harga = self.hitung_total_harga()

    # Metode untuk menghitung total harga berdasarkan jumlah dan harga produk
    def hitung_total_harga(self):
        return self.__produk.get_harga() * self.__jumlah

    # Getter untuk atribut yang diperlukan
    def get_id_transaksi(self):
        return self.__id_transaksi

    def get_produk(self):
        return self.__produk

    def get_jumlah(self):
        return self.__jumlah

    def get_total_harga(self):
        return self.__total_harga

    # Metode untuk menampilkan ringkasan transaksi (polimorfisme)
    def tampilkan_info(self):
        print(f"ID Transaksi: {self.__id_transaksi}")
        print(f"Produk: {self.__produk.get_nama()}")
        print(f"Jumlah: {self.__jumlah}")
        print(f"Total Harga: {self.__total_harga}\n")


# Kelas Kasir
class Kasir:
    def __init__(self):
        self.__daftar_transaksi = []

    # Metode untuk menambah produk ke dalam transaksi
    def tambah_produk(self, produk, jumlah):
        if produk.get_stok() >= jumlah:
            produk.set_stok(produk.get_stok() - jumlah)
            id_transaksi = f"TR-{len(self.__daftar_transaksi) + 1}"
            transaksi = Transaksi(id_transaksi, produk, jumlah)
            self.__daftar_transaksi.append(transaksi)
            print("Transaksi berhasil diproses.")
        else:
            print("Stok tidak mencukupi.")

    # Metode untuk menampilkan semua transaksi
    def tampilkan_daftar_transaksi(self):
        if self.__daftar_transaksi:
            print("\nDaftar Transaksi:")
            for transaksi in self.__daftar_transaksi:
                transaksi.tampilkan_info()
        else:
            print("Belum ada transaksi.")


# Kelas SistemInventaris
class SistemInventaris:
    def __init__(self):
        self.__daftar_produk = []

    # Metode untuk menambah produk baru ke dalam inventaris
    def tambah_produk_baru(self, id_produk, nama, kategori, harga, stok):
        produk = Produk(id_produk, nama, kategori, harga, stok)
        self.__daftar_produk.append(produk)
        print(f"Produk {nama} berhasil ditambahkan ke dalam inventaris.")

    # Metode untuk menampilkan daftar produk
    def tampilkan_daftar_produk(self):
        if self.__daftar_produk:
            print("\nDaftar Produk:")
            for produk in self.__daftar_produk:
                produk.tampilkan_info()
        else:
            print("Belum ada produk dalam inventaris.")

    # Metode untuk memproses transaksi
    def proses_transaksi(self, kasir, id_produk, jumlah):
        for produk in self.__daftar_produk:
            if produk.get_id_produk() == id_produk:
                kasir.tambah_produk(produk, jumlah)
                return
        print("Produk tidak ditemukan.")


# Fungsi utama untuk menguji program
def main():
    sistem_inventaris = SistemInventaris()
    kasir = Kasir()

    # Menambahkan beberapa produk ke dalam inventaris
    sistem_inventaris.tambah_produk_baru("P001", "Buku Tulis", "Alat Tulis", 5000, 20)
    sistem_inventaris.tambah_produk_baru("P002", "Pulpen", "Alat Tulis", 3000, 50)
    sistem_inventaris.tambah_produk_baru("P003", "Penghapus", "Alat Tulis", 2000, 30)

    # Menampilkan daftar produk
    sistem_inventaris.tampilkan_daftar_produk()

    # Memproses beberapa transaksi
    sistem_inventaris.proses_transaksi(kasir, "P001", 5)
    sistem_inventaris.proses_transaksi(kasir, "P002", 10)
    sistem_inventaris.proses_transaksi(kasir, "P003", 40)  # Transaksi gagal karena stok tidak mencukupi

    # Menampilkan daftar transaksi
    kasir.tampilkan_daftar_transaksi()

    # Menampilkan daftar produk setelah transaksi
    sistem_inventaris.tampilkan_daftar_produk()


# Menjalankan program utama
if __name__ == "__main__":
    main()