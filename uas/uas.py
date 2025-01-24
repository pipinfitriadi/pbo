class Konser:
    def __init__(self, nama, tanggal, lokasi, harga, total_tiket):
        self.nama = nama
        self.tanggal = tanggal
        self.lokasi = lokasi
        self.harga = harga
        self.total_tiket = total_tiket
        self.tiket_terjual = 0

    def sisa_tiket(self):
        return self.total_tiket - self.tiket_terjual

    def tambah_tiket_terjual(self, jumlah):
        if jumlah <= self.sisa_tiket():
            self.tiket_terjual += jumlah
            return True
        return False

    def __str__(self):
        return f"{self.nama} - {self.tanggal} - {self.lokasi} - Harga: {self.harga} - Sisa Tiket: {self.sisa_tiket()}"


class Penonton:
    def __init__(self, nama):
        self.nama = nama
        self.pemesanan = []

    def lihat_konser(self, daftar_konser):
        for konser in daftar_konser:
            print(konser)

    def pesan_tiket(self, konser, jumlah):
        if konser.tambah_tiket_terjual(jumlah):
            self.pemesanan.append((konser.nama, jumlah))
            print(f"{jumlah} tiket untuk {konser.nama} berhasil dipesan.")
        else:
            print("Maaf, tiket tidak cukup.")


class PanitiaAcara:
    def __init__(self, nama):
        self.nama = nama
        self.daftar_konser = []

    def tambah_konser(self, konser):
        self.daftar_konser.append(konser)
        print(f"Konser {konser.nama} berhasil ditambahkan.")

    def ubah_konser(self, konser, nama=None, tanggal=None, lokasi=None, harga=None, total_tiket=None):
        if nama:
            konser.nama = nama
        if tanggal:
            konser.tanggal = tanggal
        if lokasi:
            konser.lokasi = lokasi
        if harga:
            konser.harga = harga
        if total_tiket:
            konser.total_tiket = total_tiket
        print(f"Konser {konser.nama} berhasil diubah.")

    def hapus_konser(self, konser):
        self.daftar_konser.remove(konser)
        print(f"Konser {konser.nama} berhasil dihapus.")

    def lihat_tiket_terjual(self):
        for konser in self.daftar_konser:
            print(f"{konser.nama} - Tiket Terjual: {konser.tiket_terjual} - Sisa Tiket: {konser.sisa_tiket()}")


# Contoh penggunaan
if __name__ == "__main__":
    # Membuat panitia acara
    panitia = PanitiaAcara("Panitia Konser")

    # Menambahkan konser
    konser1 = Konser("Konser dosmondub", "2023-12-01", "Jakarta", 500000, 100)
    konser2 = Konser("Konser viertalle", "2023-12-05", "Bandung", 300000, 50)

    panitia.tambah_konser(konser1)
    panitia.tambah_konser(konser2)

    # Menampilkan daftar konser
    print("\nDaftar Konser:")
    panitia.lihat_tiket_terjual()

    # Membuat penonton
    penonton1 = Penonton("John Doe")

    # Penonton melihat konser
    print("\nPenonton melihat konser:")
    penonton1.lihat_konser(panitia.daftar_konser)

    # Penonton memesan tiket
    penonton1.pesan_tiket(konser1, 2)
    penonton1.pesan_tiket(konser2, 1)

    # Menampilkan status tiket terjual
    print("\nStatus Tiket Terjual:")
    panitia.lihat_tiket_terjual()