print("=====================================")
print("UTS Pemrograman Berorientasi Objek")
print("UTS Mahesa Safta Lingga S")
print("Prodi Manajemen Bisnis Digital")
print("Sistem Pengelolaan Gudang")
print("=====================================")

class Entity:
    def __init__(self, nama):
        self.nama = nama

    def tampilkan_info(self):
        pass  

class Barang(Entity):
    def __init__(self, id_barang, nama, kategori, stok):
        super().__init__(nama)  
        self.id_barang = id_barang
        self.kategori = kategori
        self.__stok = stok 

    # buat menambah stok
    def tambah_stok(self, jumlah):
        if jumlah > 0:
            self.__stok += jumlah
            print(f"Stok {self.nama} bertambah {jumlah}. Total stok: {self.__stok}")
        else:
            print("Jumlah yang ditambahkan tidak valid.")
            # untuk memastikan bahwa jumlah stock yang ditambahkan lebih dari 0 jika lebih dari 0 stok akan ditambahkan dan akan di tampilkan 

    # buat menguranggi stock
    def kurangi_stok(self, jumlah):
        if jumlah > 0 and self.__stok >= jumlah:
            self.__stok -= jumlah
            print(f"Stok {self.nama} berkurang {jumlah}. Total stok: {self.__stok}")
        else:
            print("Stok tidak mencukupi.")
            # memastiskan jika stok mencukupi dan jumlah pengurangan sesuai jika stok tidak mencukupi aakan menampilkan pesan kesalahan stok tidak mencukupi 


    # Mengambil jumlah stok
    def get_stok(self):
        return self.__stok

    # buat menampilkan informasi barang
    def tampilkan_info(self):
        return f"{self.nama} ({self.kategori}) - Stok: {self.__stok}"

# Kelas Supplier
class Supplier(Entity):
    def __init__(self, nama, kontak):
        super().__init__(nama)
        self.kontak = kontak
        self.daftar_barang = []

    # Menambah barang yang disuplai
    def tambah_barang_suplai(self, barang):
        self.daftar_barang.append(barang)
        print(f"Barang {barang.nama} ditambahkan ke daftar suplai {self.nama}.")

    # untuk menampilkan informasi supplier dan barang yang disuplai
    def tampilkan_info(self):
        print(f"Supplier: {self.nama}, Kontak: {self.kontak}")
        print("Barang yang disuplai:")
        for barang in self.daftar_barang:
            print(f"- {barang.nama}")

# Kelas Transaksi
class Transaksi:
    def __init__(self, id_transaksi, barang, jumlah, tipe):
        self.id_transaksi = id_transaksi
        self.barang = barang
        self.jumlah = jumlah
        self.tipe = tipe  # 'masuk' atau 'keluar'

    # transaksi masuk atau keluar
    def proses_transaksi(self):
        if self.tipe == 'masuk':
            self.barang.tambah_stok(self.jumlah)
        elif self.tipe == 'keluar':
            self.barang.kurangi_stok(self.jumlah)
        else:
            print("Tipe transaksi tidak valid.")
            #menambah atau mengurangi stok sesuai tipe transaksi ada barang masuk dan barang keluar

# Kelas SistemGudang
class SistemGudang:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_barang = []
        self.daftar_supplier = []

    # Menambah barang ke gudang
    def tambah_barang(self, barang):
        self.daftar_barang.append(barang)
        print(f"Barang {barang.nama} ditambahkan ke {self.nama}.")

    # Menambah supplier ke gudang
    def tambah_supplier(self, supplier):
        self.daftar_supplier.append(supplier)
        print(f"Supplier {supplier.nama} ditambahkan ke {self.nama}.")

    # Menampilkan informasi gudang (barang dan supplier)
    def tampilkan_info(self):
        print(f"\nInformasi {self.nama}")
        print("Daftar Barang:")
        for barang in self.daftar_barang:
            print(f"- {barang.tampilkan_info()}")
        print("\nDaftar Supplier:")
        for supplier in self.daftar_supplier:
            supplier.tampilkan_info()

# Membuat objek dan menguji sistem

# Membuat barang
barang1 = Barang("B001", "Pensil", "Peralatan Tulis", 50)
barang2 = Barang("B002", "Cat Air", "Peralatan Menggambar", 30)
barang3 = Barang("B003", "Penghapus", "Peralatan tulis", 19)
barang4 = Barang("B004", "Kuas", "Peralatan Menggambar", 44)
barang5 = Barang("B005", "kanvas", "Peralatan Menggambar", 40)

# Membuat supplier
supplier1 = Supplier("CV Kreatif Art", "088767868660")
supplier1.tambah_barang_suplai(barang1)
supplier1.tambah_barang_suplai(barang3)
supplier1.tambah_barang_suplai(barang5)
supplier1.tambah_barang_suplai(barang2)
supplier1.tambah_barang_suplai(barang4)


# sistem gudang
gudang = SistemGudang("Gudang Mahesa Safta Lingga S")
gudang.tambah_barang(barang1)
gudang.tambah_barang(barang2)
gudang.tambah_barang(barang3)
gudang.tambah_barang(barang4)
gudang.tambah_barang(barang5)
gudang.tambah_supplier(supplier1)

# Menampilkan informasi sistem gudang
gudang.tampilkan_info()

# Menguji transaksi
transaksi1 = Transaksi("T001", barang1, 10, "masuk")
transaksi1.proses_transaksi()

transaksi2 = Transaksi("T002", barang2, 5, "keluar")
transaksi2.proses_transaksi()

transaksi3 = Transaksi("T003", barang4, 8, "keluar")
transaksi3.proses_transaksi()

transaksi4 = Transaksi("T004", barang5, 12, "masuk")
transaksi4.proses_transaksi()

# Menampilkan informasi lagi setelah transaksi
gudang.tampilkan_info()
