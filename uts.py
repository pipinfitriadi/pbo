class Pasien:
    def __init__(self, nama, nomor_identitas, usia):
        self.__nama = nama
        self.__nomor_identitas = nomor_identitas
        self.__usia = usia
    
    def nama(self):  # Menambahkan property untuk akses nama
        return self.__nama
        
    def tampilkan_info(self):
        return f"Pasien: {self.__nama}, ID: {self.__nomor_identitas}, Usia: {self.__usia}"


class Dokter:
    def __init__(self, nama, spesialisasi):
        self.__nama = nama
        self.__spesialisasi = spesialisasi  # Perbaikan typo
        self.__jadwal = []
    
    def nama(self):  # Menambahkan property untuk akses nama
        return self.__nama
        
    def tambah_jadwal(self, janji_temu):
        self.__jadwal.append(janji_temu)  # Perbaikan akses ke variabel private


class JanjiTemu:
    def __init__(self, id_janji, pasien, dokter, waktu):
        self.__id_janji = id_janji
        self.__pasien = pasien
        self.__dokter = dokter
        self.__waktu = waktu
    
    def dokter(self):
        return self.__dokter
        
    def waktu(self):
        return self.__waktu
        
    def konfirmasi_janji(self):
        return f"Janji temu dengan {self.__pasien.nama} pada {self.__waktu} telah dikonfirmasi"


class SistemKlinik: 
    def __init__(self):
        self.__pasien_list = []
        self.__dokter_list = []
        self.__janji_temu_list = []
    
    def tambah_pasien(self, pasien):
        self.__pasien_list.append(pasien)
    
    def tambah_dokter(self, dokter):
        self.__dokter_list.append(dokter)
    
    def atur_janji_temu(self, janji_temu):
        for j in self.__janji_temu_list:
            if j.dokter == janji_temu.dokter and j.waktu == janji_temu.waktu:  # Perbaikan operator perbandingan
                return "Jadwal dokter sudah terisi. Silahkan pilih waktu lain."
        self.__janji_temu_list.append(janji_temu)
        janji_temu.dokter.tambah_jadwal(janji_temu)
        return "Janji temu berhasil diatur."

    def tampilkan_daftar_pasien(self):  # Menambahkan method untuk akses daftar
        return [pasien.tampilkan_info() for pasien in self.__pasien_list]

    def tampilkan_daftar_dokter(self):  # Menambahkan method untuk akses daftar
        return [(dokter.nama, dokter.__spesialisasi) for dokter in self.__dokter_list]

# Contoh penggunaan
sistem_klinik = SistemKlinik()  # Perbaikan nama variabel menggunakan snake_case

# Menambahkan pasien
pasien1 = Pasien("Nissy Auliyanti", "123456", 19)
sistem_klinik.tambah_pasien(pasien1)

# Menambahkan dokter
dokter1 = Dokter("Dr. Glinda", "Umum")
sistem_klinik.tambah_dokter(dokter1)

# Menampilkan daftar pasien dan dokter
print(sistem_klinik.tampilkan_daftar_pasien())
print(sistem_klinik.tampilkan_daftar_dokter())