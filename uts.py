class Pengunjung:
    def __init__(self, nama, umur, id_pengunjung):
        self.__nama = nama
        self.__umur = umur
        self.__id_pengunjung = id_pengunjung

    def tampilkan_info(self):
        return f"Nama: {self.__nama}, Umur: {self.__umur}, ID Pengunjung: {self.__id_pengunjung}"

    @property
    def umur(self):
        return self.__umur


class Wahana:
    def __init__(self, nama_wahana, deskripsi, batas_umur):
        self.__nama_wahana = nama_wahana
        self.__deskripsi = deskripsi
        self.__batas_umur = batas_umur

    def cek_batas_umur(self, pengunjung):
        return pengunjung.umur >= self.__batas_umur

    def tampilkan_info(self):
        return f"Wahana: {self.__nama_wahana}, Deskripsi: {self.__deskripsi}, Batas Umur: {self.__batas_umur}"


class Tiket:
    def __init__(self, id_tiket, pengunjung, wahana, tanggal):
        self.__id_tiket = id_tiket
        self.__pengunjung = pengunjung
        self.__wahana = wahana
        self.__tanggal = tanggal

    def validasi_tiket(self):
        return self.__wahana.cek_batas_umur(self.__pengunjung)

    def tampilkan_info(self):
        return f"Tiket ID: {self.__id_tiket}, Pengunjung: {self.__pengunjung.tampilkan_info()}, Wahana: {self.__wahana.tampilkan_info()}, Tanggal: {self.__tanggal}"


class SistemTamanBermain:
    def __init__(self):
        self.__pengunjung_list = []
        self.__wahana_list = []
        self.__tiket_list = []

    def tambah_pengunjung(self, pengunjung):
        self.__pengunjung_list.append(pengunjung)

    def tambah_wahana(self, wahana):
        self.__wahana_list.append(wahana)

    def pesan_tiket(self, id_tiket, pengunjung, wahana, tanggal):
        if wahana.cek_batas_umur(pengunjung):
            tiket = Tiket(id_tiket, pengunjung, wahana, tanggal)
            self.__tiket_list.append(tiket)
            return tiket
        else:
            raise ValueError("Pengunjung tidak memenuhi syarat batas umur untuk wahana ini.")

    def tampilkan_tiket(self):
        for tiket in self.__tiket_list:
            print(tiket.tampilkan_info())


# Contoh penggunaan
if __name__ == "__main__":
    sistem = SistemTamanBermain()

    # Menambah pengunjung
    pengunjung1 = Pengunjung("Alice", 10, "P001")
    pengunjung2 = Pengunjung("Bob", 15, "P002")
    sistem.tambah_pengunjung(pengunjung1)
    sistem.tambah_pengunjung(pengunjung2)

    # Menambah wahana
    wahana1 = Wahana("Roller Coaster", "Wahana yang sangat menegangkan", 12)
    wahana2 = Wahana("Ferris Wheel", "Wahana yang santai dan menyenangkan", 0)
    sistem.tambah_wahana(wahana1)
    sistem.tambah_wahana(wahana2)

    # Memesan tiket
    try:
        tiket1 = sistem.pesan_tiket("T001", pengunjung1, wahana1, "2023-10-01")
    except ValueError as e:
        print(e)

    tiket2 = sistem.pesan_tiket("T002", pengunjung2, wahana1, "2023-10-01")
    tiket3 = sistem.pesan_tiket("T003", pengunjung1, wahana2, "2023-10-01")

    # Menampilkan tiket
    sistem.tampilkan_tiket()