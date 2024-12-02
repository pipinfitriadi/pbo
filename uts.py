class Pengunjung:
    def __init__(self, nama, umur, id_pengunjung):
        self.__nama = nama  # Enkapsulasi: atribut disembunyikan dengan double underscore
        self.__umur = umur
        self.__id_pengunjung = id_pengunjung

    def tampilkan_info(self):
        """Menampilkan informasi pengunjung."""
        return f"ID: {self.__id_pengunjung}, Nama: {self.__nama}, Umur: {self.__umur}"


class Wahana:
    def __init__(self, nama_wahana, deskripsi, batas_umur):
        self.__nama_wahana = nama_wahana
        self.__deskripsi = deskripsi
        self.__batas_umur = batas_umur

    def cek_batas_umur(self, pengunjung):
        if pengunjung._Pengunjung__umur >= self.__batas_umur:
            return True
        return False

    def tampilkan_info(self):
        """Menampilkan informasi wahana."""
        return f"Wahana: {self.__nama_wahana}, Deskripsi: {self.__deskripsi}, Batas Umur: {self.__batas_umur} tahun"


class Tiket:
    def __init__(self, id_tiket, pengunjung, wahana, tanggal):
        self.__id_tiket = id_tiket
        self.__pengunjung = pengunjung
        self.__wahana = wahana
        self.__tanggal = tanggal

    def validasi_tiket(self):
        """Validasi apakah pengunjung dapat naik wahana."""
        if self.__wahana.cek_batas_umur(self.__pengunjung):
            return f"Tiket valid untuk {self.__pengunjung.tampilkan_info()} di {self.__wahana.tampilkan_info()} pada {self.__tanggal}."
        return f"Tiket tidak valid untuk {self.__pengunjung.tampilkan_info()} karena tidak memenuhi batas umur."


class SistemTamanBermain:
    def __init__(self):
        self.__pengunjung_list = []
        self.__wahana_list = []
        self.__tiket_list = []

    def tambah_pengunjung(self, pengunjung):
        self.__pengunjung_list.append(pengunjung)

    def tambah_wahana(self, wahana):
        self.__wahana_list.append(wahana)

    def tambah_tiket(self, tiket):
        if tiket.validasi_tiket().startswith("Tiket valid"):
            self.__tiket_list.append(tiket)
            print("Tiket berhasil dipesan.")
        else:
            print(tiket.validasi_tiket())

    def tampilkan_pengunjung(self):
        for pengunjung in self.__pengunjung_list:
            print(pengunjung.tampilkan_info())

    def tampilkan_wahana(self):
        for wahana in self.__wahana_list:
            print(wahana.tampilkan_info())

    def tampilkan_tiket(self):
        for tiket in self.__tiket_list:
            print(tiket.validasi_tiket())


# Contoh penggunaan
if __name__ == "__main__":
    # Membuat objek pengunjung
    sistem = SistemTamanBermain()

    pengunjung1 = Pengunjung("Andi", 10, "P001")
    pengunjung2 = Pengunjung("Budi", 15, "P002")

    # Menampilkan informasi pengunjung
    print(pengunjung1.tampilkan_info())
    print(pengunjung2.tampilkan_info())

    # Membuat objek wahana
    wahana1 = Wahana("Roller Coaster", "Wahana berputar cepat", 12)
    wahana2 = Wahana("Ferris Wheel", "Wahana berputar tinggi", 10)

    sistem.tambah_pengunjung(pengunjung1)
    sistem.tambah_pengunjung(pengunjung2)

    sistem.tambah_wahana(wahana1)
    sistem.tambah_wahana(wahana2)

    # Menampilkan informasi wahana
    print(wahana1.tampilkan_info())
    print(wahana2.tampilkan_info())

    # Membuat objek tiket
    tiket1 = Tiket("T001", pengunjung1, wahana1, "2023-02-20")
    tiket2 = Tiket("T002", pengunjung2, wahana1, "2023-02-20")

    sistem.tambah_tiket(tiket1)
    sistem.tambah_tiket(tiket2)

    # Validasi tiket
    print(tiket1.validasi_tiket())
    print(tiket2.validasi_tiket())
    sistem.tampilkan_pengunjung()
    sistem.tampilkan_wahana()
    sistem.tampilkan_tiket()
