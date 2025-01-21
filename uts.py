#membuat kelas barang
class BarangInventaris:
    def __init__(self, id_barang, nama_barang, kategori, jumlah, kondisi):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.kategori = kategori
        self.jumlah = jumlah
        self.kondisi = kondisi

#menampilkan info barang
    def tampilkan_info(self):
        print(f"ID Barang: {self.id_barang}")
        print(f"Nama Barang: {self.nama_barang}")
        print(f"Kategori: {self.kategori}")
        print(f"Jumlah: {self.jumlah}")
        print(f"Kondisi: {self.kondisi}")

#membuat kelas karyawan
class Karyawan:
    def __init__(self, id_karyawan, nama, jabatan):
        self.id_karyawan = id_karyawan
        self.nama = nama
        self.jabatan = jabatan

#menampilkan info karyawan
    def tampilkan_info(self):
        print(f"ID Karyawan: {self.id_karyawan}")
        print(f"Nama: {self.nama}")
        print(f"Jabatan: {self.jabatan}")

#membuat kelas peminjaman inventaris
class PeminjamanInventaris:
    def __init__(self, id_peminjaman, karyawan, barang, tanggal_pinjam, tanggal_kembali = None):
        self.id_peminjaman = id_peminjaman
        self.karyawan = karyawan
        self.barang = barang
        self.tanggal_pinjam = tanggal_pinjam
        self.tanggal_kembali = tanggal_kembali

#memvalidasi pengembalian barang
        def validasi_pengembalian(self):
            return self.tanggal_kembali is not None

#membuat kelas sistem investaris      
class SistemInventaris:
    def __init__(self):
        self.barang_list = []
        self.karyawan_list = []
        self.peminjaman_list = []

    def tambah_barang(self, barang):
        self.barang_list.append(barang)

    def tambah_karyawan(self, karyawan):
        self.karyawan_list.append(karyawan)

    def catat_peminjaman(self, peminjaman):

        if peminjaman.barang.jumlah > 0:
            peminjaman.barang.jumlah -= 1
            self.peminjaman_list.append(peminjaman)
            print("Peminjaman Berhasil Dicatat")
        else:
            print("Mohon Maaf, Barang Tidak Tersedia")

    def tampilkan_data_barang(self):
        for barang in self.barang_list:
            barang.tampilkan_info()

    def tampilkan_data_karyawan(self):
        for karyawan in self.karyawan_list:
            karyawan.tampilkan_info()

sistem = SistemInventaris()

#menambahkan data barang
barang1 = BarangInventaris("P404", "Laptop", "Perlengkapan Kantor", 20, "Baik")
barang2 = BarangInventaris("P408", "Stop Map", "Alat Tulis Kantor", 30, "Baik")
barang3 = BarangInventaris("P505", "Mesin Fotokopi", "Peralatan Kantor", 5, "Rusak")
sistem.tambah_barang(barang1)
sistem.tambah_barang(barang2)
sistem.tambah_barang(barang3)

#menambahkan data karyawan
Karyawan1 =Karyawan("046598", "Arif", "Manager")
Karyawan2 = Karyawan("046572", "Sasa", "Supervisior")
Karyawan3 = Karyawan("046597", "Icha", "Staff Marketing")
Karyawan4 = Karyawan("046588", "Abdud", "Staff Gudang")
Karyawan5 = Karyawan("046593", "Maul", "Staff HR")
sistem.tambah_karyawan(Karyawan1)
sistem.tambah_karyawan(Karyawan2)
sistem.tambah_karyawan(Karyawan3)
sistem.tambah_karyawan(Karyawan4)
sistem.tambah_karyawan(Karyawan5)

#melakukan peminjaman
peminjaman1 = PeminjamanInventaris("PI2010", Karyawan4, barang1, "2024-10-10")
sistem.catat_peminjaman(peminjaman1)

#menampilkan data barang
print("\nData Barang:")
sistem.tampilkan_data_barang()

#menampilkan data karyawan
print("\nData Karyawan:")
sistem.tampilkan_data_karyawan()

