
print ("=====================================")

print ("UTS Pemrograman Berorientasi Objeck")
print ("UTS Mahesa Safta Lingga s")
print ("Sistem Pengelolaan Gudang")

print ("====================================")

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
            print("Stok tidak mencukupi untuk transaksi ini.")

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



    
barang1 = Barang("B001", "Pensil", "Peralatan Tulis", 50)
barang2 = Barang("B002", "Cat Air", "Peralatan Menggambar", 30)

supplier1 = Supplier("CV Kreatif Art", "08123456789")
supplier1.tambah_barang_suplai(barang1)
supplier1.tambah_barang_suplai(barang2)