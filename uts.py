from datetime import datetime


class Pelanggan:
    def __init__(self, nama, nomor_identitas, umur):
        self.nama = nama
        self.nomor_identitas = nomor_identitas
        self.umur = umur

    def tampilkan_info(self):
        return f"Pelanggan: {self.nama}, ID: {self.nomor_identitas}, Umur: {self.umur} tahun"


class Kendaraan:
    def __init__(self, nomor_polisi, tipe, harga_per_hari):
        self.nomor_polisi = nomor_polisi
        self.tipe = tipe
        self.harga_per_hari = harga_per_hari
        self.status = "tersedia"

    def ubah_status(self, status):
        self.status = status

    def tampilkan_info(self):
        return f"Kendaraan: {self.tipe}, No Polisi: {self.nomor_polisi}, Harga: Rp{self.harga_per_hari}/hari, Status: {self.status}"


class Sewa:
    def __init__(self, id_sewa, pelanggan, kendaraan, tanggal_mulai, tanggal_akhir):
        self.id_sewa = id_sewa
        self.pelanggan = pelanggan
        self.kendaraan = kendaraan
        self.tanggal_mulai = datetime.strptime(tanggal_mulai, '%Y-%m-%d')
        self.tanggal_akhir = datetime.strptime(tanggal_akhir, '%Y-%m-%d')

    def hitung_biaya(self):
        durasi = (self.tanggal_akhir - self.tanggal_mulai).days + 1
        return durasi * self.kendaraan.harga_per_hari

    def tampilkan_info(self):
        return (f"Sewa ID: {self.id_sewa}\n"
                f"Pelanggan: {self.pelanggan.nama}\n"
                f"Kendaraan: {self.kendaraan.tipe} ({self.kendaraan.nomor_polisi})\n"
                f"Tanggal Mulai: {self.tanggal_mulai.date()}\n"
                f"Tanggal Akhir: {self.tanggal_akhir.date()}\n"
                f"Total Biaya: Rp{self.hitung_biaya()}")


class SistemRental:
    def __init__(self):
        self.pelanggan_list = []
        self.kendaraan_list = []
        self.sewa_list = []

    def tambah_pelanggan(self, pelanggan):
        self.pelanggan_list.append(pelanggan)

    def tambah_kendaraan(self, kendaraan):
        self.kendaraan_list.append(kendaraan)

    def sewa_kendaraan(self, id_sewa, pelanggan, nomor_polisi, tanggal_mulai, tanggal_akhir):
        for kendaraan in self.kendaraan_list:
            if kendaraan.nomor_polisi == nomor_polisi and kendaraan.status == "tersedia":
                kendaraan.ubah_status("disewa")
                sewa = Sewa(id_sewa, pelanggan, kendaraan, tanggal_mulai, tanggal_akhir)
                self.sewa_list.append(sewa)
                print(f"Kendaraan {nomor_polisi} berhasil disewa oleh {pelanggan.nama}.")
                return
        print(f"Kendaraan {nomor_polisi} tidak tersedia untuk disewa.")

    def tampilkan_pelanggan(self):
        for pelanggan in self.pelanggan_list:
            print(pelanggan.tampilkan_info())

    def tampilkan_kendaraan(self):
        for kendaraan in self.kendaraan_list:
            print(kendaraan.tampilkan_info())

    def tampilkan_sewa(self):
        for sewa in self.sewa_list:
            print(sewa.tampilkan_info())
            print("-" * 50)


rental = SistemRental()

p1 = Pelanggan("Regilia", "ID01", 19)
p2 = Pelanggan("Sherin", "ID02", 21)
p3 = Pelanggan("Najla", "ID03", 18)
p4 = Pelanggan("Adhinda", "ID04", 18)
rental.tambah_pelanggan(p1)
rental.tambah_pelanggan(p2)
rental.tambah_pelanggan(p3)
rental.tambah_pelanggan(p4)

k1 = Kendaraan("D 2611 UPR", "Mobil Mitsubishi Expander", 600000)
k2 = Kendaraan("D 1003 UT", "Motor Honda BeAT Street", 150000)
k3 = Kendaraan("D 1206 UPI", "Motor Honda Scoopy", 165000)
k4 = Kendaraan("D 0506 SMA", "Motor Yamaha XSR", 250000)
k5 = Kendaraan("D 1704 UNI", "Mobil Toyota Innova", 800000)
k6 = Kendaraan("D 2411 MBD", "Mobil Wuling Almaz", 700000)

rental.tambah_kendaraan(k1)
rental.tambah_kendaraan(k2)
rental.tambah_kendaraan(k3)
rental.tambah_kendaraan(k4)
rental.tambah_kendaraan(k5)
rental.tambah_kendaraan(k6)

rental.sewa_kendaraan("EX01", p1, "D 2611 UPR", "2024-11-24", "2024-11-27")
rental.sewa_kendaraan("EX02", p2, "D 1003 UT", "2024-11-25", "2024-11-28")
rental.sewa_kendaraan("EX03", p3, "D 1206 UPI", "2024-11-26", "2024-11-28")
rental.sewa_kendaraan("EX04", p4, "D 0506 SMA", "2024-11-29", "2024-11-30")

print("Daftar Pelanggan:")
rental.tampilkan_pelanggan()

print("Daftar Kendaraan:")
rental.tampilkan_kendaraan()

print("Daftar Sewa:")
rental.tampilkan_sewa()
