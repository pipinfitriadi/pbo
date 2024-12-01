class Pengunjung:
    def __init__(self, nama, umur, id_pengunjung):
        self.__nama = nama  # Enkapsulasi: atribut disembunyikan dengan double underscore
        self.__umur = umur
        self.__id_pengunjung = id_pengunjung

    def tampilkan_info(self):
        """Menampilkan informasi pengunjung."""
        return f"ID: {self.__id_pengunjung}, Nama: {self.__nama}, Umur: {self.__umur}"

class Wahana:
    def __init__(self, nama, tinggi_minimal):
        self.__nama = nama
        self.__tinggi_minimal = tinggi_minimal

    def tampilkan_info(self):
        """Menampilkan informasi wahana."""
        return f"Wahana: {self.__nama}, Tinggi Minimal: {self.__tinggi_minimal} cm"

class Tiket:
    def __init__(self, pengunjung, wahana):
        self.__pengunjung = pengunjung
        self.__wahana = wahana

    def validasi_tiket(self):
        """Validasi apakah pengunjung dapat naik wahana."""
        if self.__pengunjung._Pengunjung__umur < 12:
            return f"{self.__pengunjung._Pengunjung__nama} tidak dapat naik {self.__wahana._Wahana__nama} karena umur kurang dari 12 tahun."
        return f"Tiket valid untuk {self.__pengunjung._Pengunjung__nama} untuk naik {self.__wahana._Wahana__nama}."

# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek pengunjung
    pengunjung1 = Pengunjung("Andi", 10, "P001")
    pengunjung2 = Pengunjung("Budi", 15, "P002")

    # Menampilkan informasi pengunjung
    print(pengunjung1.tampilkan_info())
    print(pengunjung2.tampilkan_info())

    # Membuat objek wahana
    wahana1 = Wahana("Roller Coaster", 120)
    wahana2 = Wahana("Ferris Wheel", 100)

    # Menampilkan informasi wahana
    print(wahana1.tampilkan_info())
    print(wahana2.tampilkan_info())

    # Membuat objek tiket
    tiket1 = Tiket(pengunjung1, wahana1)
    tiket2 = Tiket(pengunjung2, wahana1)

    # Validasi tiket
    print(tiket1.validasi_tiket())
    print(tiket2.validasi_tiket())