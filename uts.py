class Pasien:
    def __init__(self, nama, nomor_identitas, usia):
        self.__nama = nama
        self.__nomor_identitas = nomor_identitas
        self.__usia = usia

    def tampilkan_info(self):
        print(f'Nama: {self.__nama}, Nomor Identitas: {self.__nomor_identitas}, Usia: {self.__usia}')

class Dokter:
    def __init__(self, nama, spesialisasi):
        self.nama = nama
        self.spesialisasi = spesialisasi
        self.jadwal = []

    def tambah_jadwal(self, janji_temu):
        self.jadwal.append(janji_temu)

class JanjiTemu:
    def __init__(self, id_janji, pasien, dokter, waktu):
        self.id_janji = id_janji
        self.pasien = pasien
        self.dokter = dokter
        self.waktu = waktu

    def konfirmasi_janji(self):
        print(f"Konfirmasi janji temu dengan {self.dokter.nama} pada waktu {self.waktu} berhasil.")

class SistemKlinik:
    def __init__(self):
        self.daftar_pasien = []
        self.daftar_dokter = []
        self.jadwal_dokter = {}

    def tambah_pasien(self, pasien):
        self.daftar_pasien.append(pasien)

    def tambah_dokter(self, dokter):
        self.daftar_dokter.append(dokter)

    def atur_janji_temu(self, janji_temu):
        dokter = janji_temu.dokter
        dokter_key = dokter.nama  # Menggunakan nama dokter sebagai kunci unik
        if dokter_key in self.jadwal_dokter:
            for jadwal in self.jadwal_dokter[dokter_key]:
                if jadwal.waktu == janji_temu.waktu:
                    print(f"Janji temu dengan {dokter.nama} pada waktu {janji_temu.waktu} sudah terjadwal.")
                    return
        else:
            self.jadwal_dokter[dokter_key] = []
        
        self.jadwal_dokter[dokter_key].append(janji_temu)
        print(f"Janji temu dengan {dokter.nama} pada waktu {janji_temu.waktu} berhasil diatur.")
        
# Contoh penggunaan program untuk sistem manajemen layanan kesehatan

# Membuat objek Pasien
pasien1 = Pasien("Nissy Auliyanti", "P001", 19)
pasien2 = Pasien("Nadin Amizah", "P002", 24)

# Menampilkan informasi pasien
pasien1.tampilkan_info()
pasien2.tampilkan_info()

# Membuat objek Dokter
dokter1 = Dokter("Dr. Glinda", "Dokter Umum")
dokter2 = Dokter("Dr. Isyana", "Dokter Spesialis")

# Menambah jadwal janji temu untuk dokter
janji_temu1 = JanjiTemu("001", pasien1, dokter1, "2024-12-12 09:00")
janji_temu2 = JanjiTemu("002", pasien2, dokter2, "2024-12-19 09:00")

dokter1.tambah_jadwal(janji_temu1)
dokter2.tambah_jadwal(janji_temu2)

# Mengatur janji temu dalam sistem klinik
sistem_klinik = SistemKlinik()
sistem_klinik.tambah_pasien(pasien1)
sistem_klinik.tambah_pasien(pasien2)
sistem_klinik.tambah_dokter(dokter1)
sistem_klinik.tambah_dokter(dokter2)
sistem_klinik.atur_janji_temu(janji_temu1)
sistem_klinik.atur_janji_temu(janji_temu2)