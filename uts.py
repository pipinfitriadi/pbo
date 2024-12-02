class Donatur:
    def __init__(self, id_donatur, nama, email):
        self.id_donatur = id_donatur
        self.nama = nama
        self.email = email

    def tampilkan_info(self):
        return f"ID Donatur: {self.id_donatur}, Nama: {self.nama}, Email: {self.email}"


class KampanyeAmal:
    def __init__(self, id_kampanye, nama_kampanye, target_donasi):
        self.id_kampanye = id_kampanye
        self.nama_kampanye = nama_kampanye
        self.target_donasi = target_donasi
        self.total_terkumpul = 0

    def tambah_donasi(self, jumlah):
        if self.total_terkumpul + jumlah > self.target_donasi:
            raise ValueError("Donasi melebihi target kampanye.")
        self.total_terkumpul += jumlah

    def tampilkan_info(self):
        return (f"ID Kampanye: {self.id_kampanye}, Nama: {self.nama_kampanye}, "
                f"Target Donasi: {self.target_donasi}, Total Terkumpul: {self.total_terkumpul}")


class Donasi:
    def __init__(self, id_donasi, donatur, kampanye, jumlah):
        self.id_donasi = id_donasi
        self.donatur = donatur
        self.kampanye = kampanye
        self.jumlah = jumlah

    def validasi_donasi(self):
        if self.jumlah <= 0:
            raise ValueError("Jumlah donasi harus lebih dari 0.")


class SistemDonasi:
    def __init__(self):
        self.daftar_donatur = {}
        self.daftar_kampanye = {}
        self.daftar_donasi = []

    def tambah_donatur(self, id_donatur, nama, email):
        if id_donatur in self.daftar_donatur:
            raise ValueError("Donatur dengan ID ini sudah ada.")
        self.daftar_donatur[id_donatur] = Donatur(id_donatur, nama, email)

    def tambah_kampanye(self, id_kampanye, nama_kampanye, target_donasi):
        if id_kampanye in self.daftar_kampanye:
            raise ValueError("Kampanye dengan ID ini sudah ada.")
        self.daftar_kampanye[id_kampanye] = KampanyeAmal(id_kampanye, nama_kampanye, target_donasi)

    def catat_donasi(self, id_donasi, id_donatur, id_kampanye, jumlah):
        if id_donatur not in self.daftar_donatur:
            raise ValueError("Donatur tidak ditemukan.")
        if id_kampanye not in self.daftar_kampanye:
            raise ValueError("Kampanye tidak ditemukan.")

        donatur = self.daftar_donatur[id_donatur]
        kampanye = self.daftar_kampanye[id_kampanye]
        donasi = Donasi(id_donasi, donatur, kampanye, jumlah)

        donasi.validasi_donasi()
        kampanye.tambah_donasi(jumlah)
        self.daftar_donasi.append(donasi)

    def tampilkan_donatur(self):
        return [donatur.tampilkan_info() for donatur in self.daftar_donatur.values()]

    def tampilkan_kampanye(self):
        return [kampanye.tampilkan_info() for kampanye in self.daftar_kampanye.values()]

    def tampilkan_donasi(self):
        return [
            f"ID Donasi: {donasi.id_donasi}, Donatur: {donasi.donatur.nama}, "
            f"Kampanye: {donasi.kampanye.nama_kampanye}, Jumlah: {donasi.jumlah}"
            for donasi in self.daftar_donasi
        ]


# Contoh Penggunaan
sistem = SistemDonasi()

# Tambah Donatur
sistem.tambah_donatur(1, "Ali", "ali@gmail.com")
sistem.tambah_donatur(2, "Budi", "budi@gmail.com")

# Tambah Kampanye
sistem.tambah_kampanye(1, "Bantuan Bencana", 100000)
sistem.tambah_kampanye(2, "Pendidikan Anak", 50000)

# Catat Donasi
sistem.catat_donasi(1, 1, 1, 25000)
sistem.catat_donasi(2, 2, 2, 20000)

# Tampilkan Data
print("Donatur:")
print(*sistem.tampilkan_donatur(), sep="\\n")

print("\\nKampanye Amal:")
print(*sistem.tampilkan_kampanye(), sep="\\n")

print("\\nDonasi:")
print(*sistem.tampilkan_donasi(), sep="\\n")
