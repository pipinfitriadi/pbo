from datetime import datetime

# Kelas Tamu
class Tamu:
    def __init__(self, id_tamu, nama, tanggal_lahir):
        self._id_tamu = id_tamu
        self._nama = nama
        self._tanggal_lahir = datetime.strptime(tanggal_lahir, '%Y-%m-%d')

    def cek_umur(self):
        today = datetime.today()
        umur = today.year - self._tanggal_lahir.year
        if today.month < self._tanggal_lahir.month or (today.month == self._tanggal_lahir.month and today.day < self._tanggal_lahir.day):
            umur -= 1
        return umur

    def __str__(self):
        return f"ID Tamu: {self._id_tamu}, Nama: {self._nama}, Umur: {self.cek_umur()} tahun"

# Kelas Kamar
class Kamar:
    def __init__(self, nomor_kamar, tipe_kamar, harga_per_malam):
        self._nomor_kamar = nomor_kamar
        self._tipe_kamar = tipe_kamar
        self._harga_per_malam = harga_per_malam
        self._status = 'tersedia'

    def ubah_status(self, status_baru):
        self._status = status_baru

    def __str__(self):
        return f"Kamar {self._nomor_kamar} - {self._tipe_kamar} - Rp{self._harga_per_malam}/malam - Status: {self._status}"

# Kelas Reservasi
class Reservasi:
    def __init__(self, id_reservasi, tamu, kamar, tanggal_checkin, tanggal_checkout):
        self._id_reservasi = id_reservasi
        self._tamu = tamu
        self._kamar = kamar
        self._tanggal_checkin = datetime.strptime(tanggal_checkin, '%Y-%m-%d')
        self._tanggal_checkout = datetime.strptime(tanggal_checkout, '%Y-%m-%d')

    def hitung_biaya(self):
        durasi = (self._tanggal_checkout - self._tanggal_checkin).days
        return durasi * self._kamar._harga_per_malam

    def __str__(self):
        return (f"Reservasi ID: {self._id_reservasi}, Tamu: {self._tamu._nama}, Kamar: {self._kamar._nomor_kamar}, "
                f"Check-in: {self._tanggal_checkin.strftime('%Y-%m-%d')}, Check-out: {self._tanggal_checkout.strftime('%Y-%m-%d')}, "
                f"Total Biaya: Rp{self.hitung_biaya()}")

# Kelas SistemHotel
class SistemHotel:
    def __init__(self):
        self._daftar_tamu = []
        self._daftar_kamar = []
        self._daftar_reservasi = []

    def tambah_tamu(self, id_tamu, nama, tanggal_lahir):
        tamu_baru = Tamu(id_tamu, nama, tanggal_lahir)
        self._daftar_tamu.append(tamu_baru)
        print(f"Tamu {nama} berhasil ditambahkan.")

    def tambah_kamar(self, nomor_kamar, tipe_kamar, harga_per_malam):
        kamar_baru = Kamar(nomor_kamar, tipe_kamar, harga_per_malam)
        self._daftar_kamar.append(kamar_baru)
        print(f"Kamar {nomor_kamar} berhasil ditambahkan.")

    def buat_reservasi(self, id_reservasi, id_tamu, nomor_kamar, tanggal_checkin, tanggal_checkout):
        tamu = next((t for t in self._daftar_tamu if t._id_tamu == id_tamu), None)
        kamar = next((k for k in self._daftar_kamar if k._nomor_kamar == nomor_kamar), None)

        if not tamu:
            print("Tamu tidak ditemukan.")
            return

        if not kamar:
            print("Kamar tidak ditemukan.")
            return

        if kamar._status != 'tersedia':
            print("Kamar tidak tersedia.")
            return

        reservasi_baru = Reservasi(id_reservasi, tamu, kamar, tanggal_checkin, tanggal_checkout)
        self._daftar_reservasi.append(reservasi_baru)
        kamar.ubah_status('dipesan')
        print(f"Reservasi berhasil dibuat untuk {tamu._nama} di kamar {kamar._nomor_kamar}.")

    def lihat_tamu(self):
        if not self._daftar_tamu:
            print("Belum ada tamu yang terdaftar.")
            return
        for tamu in self._daftar_tamu:
            print(tamu)

    def lihat_kamar(self):
        if not self._daftar_kamar:
            print("Belum ada kamar yang tersedia.")
            return
        for kamar in self._daftar_kamar:
            print(kamar)

    def lihat_reservasi(self):
        if not self._daftar_reservasi:
            print("Belum ada reservasi.")
            return
        for reservasi in self._daftar_reservasi:
            print(reservasi)


hotel = SistemHotel()

# Menambahkan tamu
hotel.tambah_tamu('T001', 'Marselino', '2002-04-19')
hotel.tambah_tamu('T002', 'manchester united', '1822-06-17')

# Menambahkan kamar
hotel.tambah_kamar(101, 'Deluxe', 500000)
hotel.tambah_kamar(102, 'Superior', 400000)

# Melihat daftar tamu dan kamar
print("\nDaftar Tamu:")
hotel.lihat_tamu()

print("\nDaftar Kamar:")
hotel.lihat_kamar()

# Membuat reservasi
hotel.buat_reservasi('R001', 'T001', 101, '2024-11-29', '2024-12-02')
hotel.buat_reservasi('R001', 'T002', 102, '2024-11-29', '2024-12-02')

# Melihat daftar reservasi
print("\nDaftar Reservasi:")
hotel.lihat_reservasi()

