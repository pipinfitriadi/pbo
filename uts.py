class Film:
    def __init__(self, judul, genre, durasi, batas_umur):
        self.__judul = judul
        self.__genre = genre
        self.__durasi = durasi
        self.__batas_umur = batas_umur  # Batas umur film (misalnya PG-13)

    def tampilkan_info(self):
        return f"Judul: {self.__judul}, Genre: {self.__genre}, Durasi: {self.__durasi} menit, Batas Umur: {self.__batas_umur}"

    def get_batas_umur(self):
        return self.__batas_umur

    def get_judul(self):
        return self.__judul


class Penonton:
    def __init__(self, nama, umur, id_penonton):
        self.__nama = nama
        self.__umur = umur
        self.__id_penonton = id_penonton

    def cek_batas_umur(self, film):
        batas_umur = film.get_batas_umur()
        if batas_umur == "PG-13":
            return self.__umur >= 13
        elif batas_umur == "R":
            return self.__umur >= 17
        return True  # Default untuk film tanpa batasan umur

    def get_nama(self):
        return self.__nama


class Tiket:
    def __init__(self, id_tiket, film, penonton, waktu):
        self.__id_tiket = id_tiket
        self.__film = film
        self.__penonton = penonton
        self.__waktu = waktu

    def validasi_tiket(self):
        return self.__penonton.cek_batas_umur(self.__film)


class SistemBioskop:
    def __init__(self):
        self.__daftar_film = []
        self.__daftar_penonton = []
        self.__daftar_tiket = []

    def tambah_film(self, film):
        self.__daftar_film.append(film)

    def tambah_penonton(self, penonton):
        self.__daftar_penonton.append(penonton)

    def buat_tiket(self, id_tiket, film, penonton, waktu):
        if penonton.cek_batas_umur(film):
            tiket = Tiket(id_tiket, film, penonton, waktu)
            self.__daftar_tiket.append(tiket)
            return f"Tiket berhasil dibuat. Id Tiket : {id_tiket},Nama : {penonton.get_nama()}, Film : {film.get_judul()}, Waktu : {waktu}."
        else:
            return f"Tiket tidak dapat dibuat. {penonton.get_nama()} tidak memenuhi batas umur untuk film {film.get_judul()}."


# Contoh penggunaan
if __name__ == "__main__":
    bioskop = SistemBioskop()

    film1 = Film("Avengers", "Action", 180, "PG-13")
    film2 = Film("AADC (Ada Apa Dengan Cinta)", "Drama", 120, "R")

    bioskop.tambah_film(film1)
    bioskop.tambah_film(film2)

    penonton1 = Penonton("Siti", 14, "P001")
    penonton2 = Penonton("Sunjae", 16, "P002")
    penonton3 = Penonton("Kyungso", 12, "P003")

    bioskop.tambah_penonton(penonton1)
    bioskop.tambah_penonton(penonton2)
    bioskop.tambah_penonton(penonton3)

    print(bioskop.buat_tiket("T001", film1, penonton1, "19:00"))
    print(bioskop.buat_tiket("T002", film2, penonton2, "21:00"))
    print(bioskop.buat_tiket("T003", film1, penonton3, "22:00"))