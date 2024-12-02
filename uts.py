
class Pasien:
    def __init__(self, nama, nomor_identitas, usia):
        self.__nama = nama
        self.__nomor_identitas = nomor_identitas
        self.__usia = usia
    def tampilkan_info(self):
        return f"Pasien: {self.__nama}, ID: {self.__nomor_identitas}, Usia: {self.__usia}"


class Dokter:
    def __init__(self, nama, spesialisasi):
        self.__nama = nama
        self.__spealisasi = spesialisasi
        self.__jadwal = []
    def tambah_jadwal(self, janji_temu):
        self.jadwal.append(janji_temu)

class JanjiTemu:
    def __init__(self, id_janji, pasien, dokter, waktu):
        self.__id_janji = id_janji
        self.__pasien = pasien
        self.__dokter = dokter
        self.__waktu =waktu
    def konfirmasi_janji(self):
        return f"janji temu dengan {self. __pasien.__nama} pada {self.__waktu} telah dikonfirmasi"

class SistemKlinik: 
    def __init__(self):
        self.__pasien_list =[]
        self.__dokter_list =[]
        self.__janji_temu_list =[]
    def tambah_pasien(self, pasien):
        self.__pasien_list.append(pasien)
    def tambah_dokter(self, dokter):
        self.__dokter_list.append(dokter)
    def atur_janji_temu(self, janji_temu):
        for j in self.__janji_temu_list:
            if j.dokter = janji_temu.dokter and j.waktu = janji_temu.waktu
                return "Jadwal dokter sudah terisi. Silahkan pilih waktu lain."
        self.__janji_temu_list.append(janji_temu)
        janji_temu.dokter.tambah_jadwal(janji_temu)
        return "Janji temu berhasil diatur."

# contoh penggunaan
Sistem_Klinik = SistemKlinik()

# menambahkan pasien
pasien1 = Pasien("Nissy Auliyanti", "123456", 19)
Sistem_Klinik.tambah_pasien(pasien1)

# menambahkan dokter
dokter1 = Dokter("Dr. Glinda", "Umum")
Sistem_Klinik.tambah_dokter(dokter1)

# menampilkan daftar pasien dan dokter
print([pasien.tampil_info() for pasien in Sistem_Klinik.__pasien_list])
print([(dokter.nama, dokter.spesialisasi) for dokter in Sistem_Klinik.__dokter_list])

