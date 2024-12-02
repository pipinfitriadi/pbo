from datetime import datetime

# UTS_AHMAD FAUZI SIMATUPANG

# Kelas Pelanggan

class Pelanggan:
    def __init__(self, nama, nomor_telepon):
        self.__nama = nama
        self.__nomor_telepon = nomor_telepon
        self.__reservasi = []

    def tambah_reservasi(self, reservasi):
        self.__reservasi.append(reservasi)

    @property
    def nama(self):
        return self.__nama

    @property
    def nomor_telepon(self):
        return self.__nomor_telepon

    def tampilkan_reservasi(self):
        return [str(r) for r in self.__reservasi]

# Kelas Meja
class Meja:
    def __init__(self, nomor_meja, kapasitas):
        self.__nomor_meja = nomor_meja
        self.__kapasitas = kapasitas
        self.__status = True

    def tampilkan_info(self):
        status = "Tersedia" if self.__status else "Tidak Tersedia"
        return f"Meja {self.__nomor_meja}, Kapasitas: {self.__kapasitas}, Status: {status}"

    def ubah_status(self, status):
        self.__status = status

    @property
    def nomor_meja(self):
        return self.__nomor_meja

    @property
    def kapasitas(self):
        return self.__kapasitas

    @property
    def status(self):
        return self.__status

# Kelas Reservasi
class Reservasi:
    def __init__(self, id_reservasi, pelanggan, meja, tanggal_waktu):
        self.__id_reservasi = id_reservasi
        self.__pelanggan = pelanggan
        self.__meja = meja
        self.__tanggal_waktu = tanggal_waktu

    def konfirmasi_reservasi(self):
        if self.__meja.status:
            self.__meja.ubah_status(False)
            self.__pelanggan.tambah_reservasi(self)
            return True
        return False

    def __str__(self):
        return (f"Reservasi ID: {self.__id_reservasi}, Pelanggan: {self.__pelanggan.nama}, "
                f"Meja: {self.__meja.nomor_meja}, Tanggal/Waktu: {self.__tanggal_waktu}")

# Kelas SistemRestoran
class SistemRestoran:
    def __init__(self):
        self.__pelanggan_list = []
        self.__meja_list = []
        self.__reservasi_list = []

    def tambah_pelanggan(self, nama, nomor_telepon):
        pelanggan = Pelanggan(nama, nomor_telepon)
        self.__pelanggan_list.append(pelanggan)
        return pelanggan

    def tambah_meja(self, nomor_meja, kapasitas):
        meja = Meja(nomor_meja, kapasitas)
        self.__meja_list.append(meja)
        return meja

    def buat_reservasi(self, pelanggan, nomor_meja, tanggal_waktu):
        meja = next((meja for meja in self.__meja_list if meja.nomor_meja == nomor_meja), None)
        if meja and meja.status:
            id_reservasi = len(self.__reservasi_list) + 1
            reservasi = Reservasi(id_reservasi, pelanggan, meja, tanggal_waktu)
            if reservasi.konfirmasi_reservasi():
                self.__reservasi_list.append(reservasi)
                return reservasi
        return "Meja tidak tersedia atau tidak ditemukan."

    def tampilkan_pelanggan(self):
        return [f"{p.nama}, Nomor Telepon: {p.nomor_telepon}" for p in self.__pelanggan_list]

    def tampilkan_meja(self):
        return [meja.tampilkan_info() for meja in self.__meja_list]

# Contoh Penggunaan
if __name__ == "__main__":
    restoran = SistemRestoran()

    pelanggan1 = restoran.tambah_pelanggan("Alice", "08123456789")
    pelanggan2 = restoran.tambah_pelanggan("Bob", "08198765432")

    restoran.tambah_meja(1, 4)
    restoran.tambah_meja(2, 2)

    waktu_reservasi = datetime(2024, 12, 1, 19, 0)

    reservasi1 = restoran.buat_reservasi(pelanggan1, 1, waktu_reservasi)
    print(reservasi1)

    reservasi2 = restoran.buat_reservasi(pelanggan2, 1, waktu_reservasi)
    print(reservasi2)

    print("Daftar Pelanggan:")
    for p in restoran.tampilkan_pelanggan():
        print(p)

    print("Daftar Meja:")
    for m in restoran.tampilkan_meja():
        print(m)
