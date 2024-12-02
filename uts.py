from datetime import datetime

class Penumpang:
    def __init__(self, nama, nomor_paspor, tanggal_lahir):
        self.nama = nama
        self.nomor_paspor = nomor_paspor
        self.tanggal_lahir = datetime.strptime(tanggal_lahir, '%Y-%m-%d')
    
    def cek_umur(self):
        """Menghitung umur berdasarkan tanggal lahir"""
        hari_ini = datetime.today()
        umur = hari_ini.year - self.tanggal_lahir.year
        if hari_ini.month < self.tanggal_lahir.month or (hari_ini.month == self.tanggal_lahir.month and hari_ini.day < self.tanggal_lahir.day):
            umur -= 1
        return umur

class Penerbangan:
    def __init__(self, nomor_penerbangan, asal, tujuan, jadwal_berangkat, kapasitas):
        self.nomor_penerbangan = nomor_penerbangan
        self.asal = asal
        self.tujuan = tujuan
        self.jadwal_berangkat = datetime.strptime(jadwal_berangkat, '%Y-%m-%d %H:%M')
        self.kapasitas = kapasitas
        self.penumpang = []
    
    def tampilkan_info(self):
        """Menampilkan informasi penerbangan"""
        print(f"Penerbangan {self.nomor_penerbangan} ({self.asal} -> {self.tujuan})")
        print(f"Jadwal Berangkat: {self.jadwal_berangkat.strftime('%Y-%m-%d %H:%M')}")
        print(f"Kapasitas: {self.kapasitas} penumpang")
        print(f"Jumlah Penumpang Saat Ini: {len(self.penumpang)}")
    
    def tambah_penumpang(self, penumpang):
        """Menambah penumpang ke penerbangan jika kapasitas masih ada"""
        if len(self.penumpang) < self.kapasitas:
            self.penumpang.append(penumpang)
            return True
        return False

class TiketPesawat:
    def __init__(self, id_tiket, penumpang, penerbangan, nomor_kursi):
        self.id_tiket = id_tiket
        self.penumpang = penumpang
        self.penerbangan = penerbangan
        self.nomor_kursi = nomor_kursi
    
    def validasi_tiket(self):
        """Memastikan tiket valid (penumpang dan penerbangan sesuai)"""
        if self.penumpang in self.penerbangan.penumpang:
            return True
        return False

class SistemPemesananTiket:
    def __init__(self):
        self.penumpang_list = []
        self.penerbangan_list = []
        self.tiket_list = []
    
    def tambah_penumpang(self, nama, nomor_paspor, tanggal_lahir):
        """Menambah penumpang baru ke sistem"""
        penumpang = Penumpang(nama, nomor_paspor, tanggal_lahir)
        self.penumpang_list.append(penumpang)
        return penumpang
    
    def tambah_penerbangan(self, nomor_penerbangan, asal, tujuan, jadwal_berangkat, kapasitas):
        """Menambah penerbangan baru ke sistem"""
        penerbangan = Penerbangan(nomor_penerbangan, asal, tujuan, jadwal_berangkat, kapasitas)
        self.penerbangan_list.append(penerbangan)
        return penerbangan
    
    def pesan_tiket(self, id_tiket, penumpang, penerbangan, nomor_kursi):
        """Memesan tiket untuk penumpang pada penerbangan tertentu"""
        if penerbangan.tambah_penumpang(penumpang):
            tiket = TiketPesawat(id_tiket, penumpang, penerbangan, nomor_kursi)
            self.tiket_list.append(tiket)
            return tiket
        else:
            print(f"Penerbangan {penerbangan.nomor_penerbangan} sudah penuh!")
            return None
if __name__ == "__main__":
    sistem = SistemPemesananTiket()

    penumpang1 = sistem.tambah_penumpang("UCUP TENGKUREP", "A1234567", "2004-05-25")
    penumpang2 = sistem.tambah_penumpang("MAS RUSDY", "B2345678", "2005-05-25")

    penerbangan1 = sistem.tambah_penerbangan("GA123", "tasikmalaya", "gaza", "2024-12-2 08:00", 2)

    penerbangan1.tampilkan_info()

    tiket1 = sistem.pesan_tiket("T001", penumpang1, penerbangan1, "12A")
    tiket2 = sistem.pesan_tiket("T002", penumpang2, penerbangan1, "12B")

    if tiket1 and tiket1.validasi_tiket():
        print(f"Tiket 1: {tiket1.id_tiket}, Penumpang: {tiket1.penumpang.nama}, Kursi: {tiket1.nomor_kursi}, Umur: {tiket1.penumpang.cek_umur()} tahun")
    if tiket2 and tiket2.validasi_tiket():
        print(f"Tiket 2: {tiket2.id_tiket}, Penumpang: {tiket2.penumpang.nama}, Kursi: {tiket2.nomor_kursi}, Umur: {tiket2.penumpang.cek_umur()} tahun")

    penumpang3 = sistem.tambah_penumpang("mas rusdy", "C3456789", "1988-11-20")
    tiket3 = sistem.pesan_tiket("T003", penumpang3, penerbangan1, "12C")

    if tiket3 and tiket3.validasi_tiket():
        print(f"Tiket 3: {tiket3.id_tiket}, Penumpang: {tiket3.penumpang.nama}, Kursi: {tiket3.nomor_kursi}, Umur: {tiket3.penumpang.cek_umur()} tahun")
    else:
        print(f"Penerbangan {penerbangan1.nomor_penerbangan} sudah penuh. Tiket tidak bisa dipesan.")

