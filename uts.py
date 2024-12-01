print("=====================================")
print("UTS Pemrograman Berorientasi Objek")
print("UTS Mahesa Safta Lingga S")
print("Prodi Manajemen Bisnis Digital")
print("Sistem Pengelolaan Gudang")
print("=====================================")

class Barang: 
    def __init__(self, id_barang, nama, kategori, stok):
        self.id_barang = id_barang
        self.nama = nama
        self.kategori = kategori
        self.__stok = stok  

    def tambah_stok(self, jumlah):
        self.__stok += jumlah
        print(f"Stok {self.nama} bertambah {jumlah}. Total stok: {self.__stok}")

    def kurangi_stok(self, jumlah):
        if self.__stok >= jumlah:
            self.__stok -= jumlah
            print(f"Stok {self.nama} berkurang {jumlah}. Total stok: {self.__stok}")
        else:
            print("Stok tidak mencukupi / stok sedang kosong.")

    def tampilkan_info(self):
        return f"{self.nama} ({self.kategori}) - Stok: {self.__stok}"  

class Supplier:
    def __init__(self, nama, kontak):
        self.nama = nama
        self.kontak = kontak
        self.daftar_barang = []

    def tambah_barang_suplai(self, barang):
        self.daftar_barang.append(barang)
        print(f"Barang {barang.nama} ditambahkan ke daftar suplai {self.nama}.")

    def tampilkan_info(self):
        print(f"Supplier: {self.nama}, Kontak: {self.kontak}")
        print("Barang yang disuplai:")
        for barang in self.daftar_barang:
            print(f"- {barang.nama}")

class Transaksi:
    def __init__(self, id_transaksi, barang, jumlah, tipe):
        self.id_transaksi = id_transaksi
        self.barang = barang
        self.jumlah = jumlah
        self.tipe = tipe  # 'masuk' atau 'keluar'

    def proses_transaksi(self):
        if self.tipe == 'masuk':
            self.barang.tambah_stok(self.jumlah)
        elif self.tipe == 'keluar':
            self.barang.kurangi_stok(self.jumlah)
        else:
            print("Tipe transaksi tidak valid.")

# Menambahkan kelas SistemGudang
class SistemGudang:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_barang = []
        self.daftar_supplier = []

    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)
        print(f"Barang {barang.nama} ditambahkan ke {self.nama}.")

    def tambah_supplier(self, supplier):
        self.daftar_supplier.append(supplier)
        print(f"Supplier {supplier.nama} ditambahkan ke {self.nama}.")

    def tampilkan_info(self):
        print(f"\nInformasi {self.nama}")
        print("Daftar Barang:")
        for barang in self.daftar_barang:
            print(f"- {barang.tampilkan_info()}")
        print("\nDaftar Supplier:")
        for supplier in self.daftar_supplier:
            supplier.tampilkan_info()

# Membuat objek dan menguji sistem
barang1 = Barang("B001", "Pensil", "Peralatan Tulis", 50)
barang2 = Barang("B002", "Cat Air", "Peralatan Menggambar", 30)

supplier1 = Supplier("CV Kreatif Art", "08123456789")
supplier1.tambah_barang_suplai(barang1)
supplier1.tambah_barang_suplai(barang2)

gudang = SistemGudang("Gudang Mahesa Safta Lingga S")
gudang.tambah_barang(barang1)
gudang.tambah_barang(barang2)
gudang.tambah_supplier(supplier1)

# Menampilkan informasi sistem gudang
gudang.tampilkan_info()
