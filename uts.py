from datetime import datetime, timedelta

class Buku:
    def __init__(self, isbn, judul, pengarang, jumlah_eksemplar):
        self.isbn = isbn
        self.judul = judul
        self.pengarang = pengarang
        self.jumlah_eksemplar = jumlah_eksemplar

    def tampilkan_info(self):
        print(f"ISBN       : {self.isbn}")
        print(f"Judul      : {self.judul}")
        print(f"Pengarang  : {self.pengarang}")
        print(f"Jumlah Eksemplar: {self.jumlah_eksemplar}")

    def tersedia(self):
        return self.jumlah_eksemplar > 0

    def pinjam(self):
        if self.tersedia():
            self.jumlah_eksemplar -= 1
            return True
        return False

    def kembalikan(self):
        self.jumlah_eksemplar += 1


class Anggota:
    def __init__(self, id_anggota, nama):
        self.id_anggota = id_anggota
        self.nama = nama
        self.buku_dipinjam = []

    def pinjam_buku(self, buku):
        if buku.pinjam():
            self.buku_dipinjam.append(buku)
            print(f"{self.nama} berhasil meminjam buku {buku.judul}.")
        else:
            print(f"Buku {buku.judul} tidak tersedia untuk dipinjam.")

    def kembalikan_buku(self, buku):
        if buku in self.buku_dipinjam:
            buku.kembalikan()
            self.buku_dipinjam.remove(buku)
            print(f"{self.nama} berhasil mengembalikan buku {buku.judul}.")
        else:
            print(f"{self.nama} tidak meminjam buku {buku.judul}.")


class Peminjaman:
    def __init__(self, id_peminjaman, anggota, buku, tanggal_peminjaman):
        self.id_peminjaman = id_peminjaman
        self.anggota = anggota
        self.buku = buku
        self.tanggal_peminjaman = tanggal_peminjaman

    def cek_keterlambatan(self, tanggal_kembali):
        batas_waktu = self.tanggal_peminjaman + timedelta(days=7)
        if tanggal_kembali > batas_waktu:
            keterlambatan = (tanggal_kembali - batas_waktu).days
            return keterlambatan
        return 0


class SistemPerpustakaan:
    def __init__(self):
        self.buku_list = []
        self.anggota_list = []
        self.peminjaman_list = []

    def tambah_buku(self, buku):
        self.buku_list.append(buku)
        print(f"Buku {buku.judul} telah ditambahkan ke perpustakaan.")

    def tambah_anggota(self, anggota):
        self.anggota_list.append(anggota)
        print(f"Anggota {anggota.nama} telah terdaftar di perpustakaan.")

    def pinjam_buku(self, id_anggota, isbn_buku):
        anggota = self._find_anggota(id_anggota)
        buku = self._find_buku(isbn_buku)

        if anggota and buku:
            anggota.pinjam_buku(buku)
            peminjaman = Peminjaman(len(self.peminjaman_list) + 1, anggota, buku, datetime.now())
            self.peminjaman_list.append(peminjaman)
        else:
            print("Peminjaman gagal. Anggota atau buku tidak ditemukan.")

    def kembalikan_buku(self, id_anggota, isbn_buku, tanggal_kembali):
        anggota = self._find_anggota(id_anggota)
        buku = self._find_buku(isbn_buku)

        if anggota and buku:
            anggota.kembalikan_buku(buku)
            peminjaman = self._find_peminjaman(anggota, buku)
            if peminjaman:
                keterlambatan = peminjaman.cek_keterlambatan(tanggal_kembali)
                if keterlambatan > 0:
                    print(f"Buku {buku.judul} dikembalikan terlambat {keterlambatan} hari.")
                else:
                    print(f"Buku {buku.judul} dikembalikan tepat waktu.")
        else:
            print("Pengembalian gagal. Anggota atau buku tidak ditemukan.")

    def _find_anggota(self, id_anggota):
        for anggota in self.anggota_list:
            if anggota.id_anggota == id_anggota:
                return anggota
        return None

    def _find_buku(self, isbn_buku):
        for buku in self.buku_list:
            if buku.isbn == isbn_buku:
                return buku
        return None

    def _find_peminjaman(self, anggota, buku):
        for peminjaman in self.peminjaman_list:
            if peminjaman.anggota == anggota and peminjaman.buku == buku:
                return peminjaman
        return None



buku1 = Buku("978-3-16-148410-0", "Pemrograman Python", "arya", 5)
buku2 = Buku("978-1-23-456789-7", "Algoritma dan Struktur Data", "ari", 2)


anggota1 = Anggota(1, "ali albuni")
anggota2 = Anggota(2, "wilson")


sistem = SistemPerpustakaan()

sistem.tambah_buku(buku1)
sistem.tambah_buku(buku2)
sistem.tambah_anggota(anggota1)
sistem.tambah_anggota(anggota2)

sistem.pinjam_buku(1, "978-3-16-148410-0")
sistem.pinjam_buku(2, "978-1-23-456789-7")

sistem.kembalikan_buku(1, "978-3-16-148410-0", datetime.now() + timedelta(days=5))  
sistem.kembalikan_buku(2, "978-1-23-456789-7", datetime.now() + timedelta(days=10))  
