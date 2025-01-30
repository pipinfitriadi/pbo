from datetime import datetime

print("RESERVASI HOTEL @Dimas_club")

# Kelas Dasar Person
class Person:
    def __init__(self, nama, nomor_telepon):
        self.nama = nama
        self.nomor_telepon = nomor_telepon

    def tampilkan_info(self):
        """Metode untuk menampilkan informasi dasar orang (tamu)."""
        print(f"Nama: {self.nama}")
        print(f"Nomor Telepon: {self.nomor_telepon}")

# Kelas Tamu (Turunan dari Person)
class Tamu(Person):
    def __init__(self, nama, nomor_telepon, id_tamu):
        super().__init__(nama, nomor_telepon)  # Memanggil konstruktor dari kelas induk
        self.id_tamu = id_tamu
        self.reservasi = []

    def tambah_reservasi(self, reservasi):
        """Menambahkan reservasi ke daftar reservasi tamu."""
        self.reservasi.append(reservasi)

    def tampilkan_info(self):
        """Override untuk menampilkan info tamu lebih lengkap."""
        super().tampilkan_info()
        print(f"ID Tamu: {self.id_tamu}")
        print(f"Jumlah Reservasi: {len(self.reservasi)}")

# Kelas Kamar
class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar, harga_per_malam):
        self.nomor_kamar = nomor_kamar
        self.tipe_kamar = tipe_kamar
        self.harga_per_malam = harga_per_malam
        self._tersedia = True  # Menyembunyikan status ketersediaan kamar dengan enkapsulasi

    def tampilkan_info(self):
        """Menampilkan informasi kamar."""
        print(f"Nomor Kamar: {self.nomor_kamar}")
        print(f"Tipe Kamar: {self.tipe_kamar}")
        print(f"Harga per Malam: {self.harga_per_malam}")
        print(f"Ketersediaan: {'Tersedia' if self._tersedia else 'Tidak Tersedia'}")

    def set_tersedia(self, status):
        """Mengubah status ketersediaan kamar."""
        self._tersedia = status

    def get_tersedia(self):
        """Mengecek apakah kamar tersedia."""
        return self._tersedia

# Kelas Reservasi
class Reservasi:
    def __init__(self, id_reservasi, tamu, kamar, tanggal_check_in, tanggal_check_out):
        self.id_reservasi = id_reservasi
        self.tamu = tamu
        self.kamar = kamar
        self.tanggal_check_in = tanggal_check_in
        self.tanggal_check_out = tanggal_check_out

    def hitung_total_harga(self):
        """Menghitung total harga berdasarkan durasi menginap."""
        durasi = (self.tanggal_check_out - self.tanggal_check_in).days
        return durasi * self.kamar.harga_per_malam

    def tampilkan_info(self):
        """Menampilkan detail informasi reservasi."""
        print(f"ID Reservasi: {self.id_reservasi}")
        print(f"Tamu: {self.tamu.nama}")
        print(f"Kamar: {self.kamar.nomor_kamar} - {self.kamar.tipe_kamar}")
        print(f"Check-in: {self.tanggal_check_in.strftime('%Y-%m-%d')}")
        print(f"Check-out: {self.tanggal_check_out.strftime('%Y-%m-%d')}")
        print(f"Total Harga: {self.hitung_total_harga()}")

# Kelas SistemHotel
class SistemHotel:
    def __init__(self):
        self.tamu_list = []  # Daftar tamu
        self.kamar_list = []  # Daftar kamar
        self.reservasi_list = []  # Daftar reservasi

    def tambah_tamu(self, tamu):
        """Menambahkan tamu ke daftar tamu."""
        self.tamu_list.append(tamu)

    def hapus_tamu(self, id_tamu):
        """Menghapus tamu berdasarkan ID."""
        self.tamu_list = [tamu for tamu in self.tamu_list if tamu.id_tamu != id_tamu]

    def tambah_kamar(self, kamar):
        """Menambahkan kamar ke daftar kamar."""
        self.kamar_list.append(kamar)

    def hapus_kamar(self, nomor_kamar):
        """Menghapus kamar berdasarkan nomor kamar."""
        self.kamar_list = [kamar for kamar in self.kamar_list if kamar.nomor_kamar != nomor_kamar]

    def tampilkan_kamar_tersedia(self):
        """Menampilkan kamar yang tersedia."""
        print("Kamar yang Tersedia:")
        for kamar in self.kamar_list:
            if kamar.get_tersedia():
                kamar.tampilkan_info()

    def tampilkan_tamu_terdaftar(self):
        """Menampilkan tamu yang terdaftar."""
        print("Daftar Tamu Terdaftar:")
        for tamu in self.tamu_list:
            tamu.tampilkan_info()

    def buat_reservasi(self, id_reservasi, id_tamu, nomor_kamar, tanggal_check_in, tanggal_check_out):
        """Membuat reservasi untuk tamu jika kamar tersedia."""
        tamu = next((tamu for tamu in self.tamu_list if tamu.id_tamu == id_tamu), None)
        kamar = next((kamar for kamar in self.kamar_list if kamar.nomor_kamar == nomor_kamar), None)

        if tamu and kamar and kamar.get_tersedia():
            # Membuat reservasi baru
            reservasi = Reservasi(id_reservasi, tamu, kamar, tanggal_check_in, tanggal_check_out)
            tamu.tambah_reservasi(reservasi)
            kamar.set_tersedia(False)  # Kamar menjadi tidak tersedia setelah reservasi
            self.reservasi_list.append(reservasi)
            print("Reservasi berhasil dibuat!")
            reservasi.tampilkan_info()
        else:
            print("Reservasi gagal! Kamar tidak tersedia atau tamu tidak ditemukan.")

# Contoh Penggunaan Program
hotel = SistemHotel()

# Menambah kamar
kamar1 = Kamar(101, "Standar", 500000)
kamar2 = Kamar(102, "Deluxe", 800000)
kamar3 = Kamar(103, "Suite",1000000)
hotel.tambah_kamar(kamar1)
hotel.tambah_kamar(kamar2)
hotel.tambah_kamar(kamar3)

# Menambah tamu
tamu1 = Tamu("Dimas alexander", "08123456789", 1)
tamu2 = Tamu("Ratna Komalla", "08234567890", 2)
tamu3 = Tamu("Cahyo", "0853429490", 3)
hotel.tambah_tamu(tamu1)
hotel.tambah_tamu(tamu2)
hotel.tambah_tamu(tamu3)

# Menampilkan kamar yang tersedia
hotel.tampilkan_kamar_tersedia()

# Membuat reservasi
tanggal_check_in = datetime(2024, 12, 1)
tanggal_check_out = datetime(2024, 12, 5)
hotel.buat_reservasi(1, 1, 101, tanggal_check_in, tanggal_check_out)

# Menampilkan tamu terdaftar
hotel.tampilkan_tamu_terdaftar()

# Menampilkan kamar yang tersedia setelah reservasi
hotel.tampilkan_kamar_tersedia()