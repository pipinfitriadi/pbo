from datetime import date

# Kelas Pengunjung
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

    @property
    def nama(self):
        return self.__nama

    @property
    def id_pengunjung(self):
        return self.__id_pengunjung

    @umur.setter
    def umur(self, umur):
        if umur < 0:
            raise ValueError("Umur tidak boleh negatif.")
        self.__umur = umur


# Kelas Wahana
class Wahana:
    def __init__(self, nama_wahana, deskripsi, batas_umur):
        self.__nama_wahana = nama_wahana
        self.__deskripsi = deskripsi
        self.__batas_umur = batas_umur

    def cek_batas_umur(self, pengunjung):
        return pengunjung.umur >= self.__batas_umur

    def tampilkan_info(self):
        return f"Wahana: {self.__nama_wahana}, Deskripsi: {self.__deskripsi}, Batas Umur: {self.__batas_umur}"


# Kelas Tiket
class Tiket:
    def __init__(self, id_tiket, pengunjung, wahana, tanggal):
        self.__id_tiket = id_tiket
        self.__pengunjung = pengunjung
        self.__wahana = wahana
        self.__tanggal = tanggal

    def validasi_tiket(self):
        return self.__wahana.cek_batas_umur(self.__pengunjung)

    def tampilkan_info(self):
        return (
            f"Tiket ID: {self.__id_tiket}, Pengunjung: {self.__pengunjung.nama}, "
            f"Wahana: {self.__wahana.tampilkan_info()}, Tanggal: {self.__tanggal}"
        )


# Kelas SistemTamanBermain
class SistemTamanBermain:
    def __init__(self):
        self.__pengunjung_list = []
        self.__wahana_list = []
        self.__tiket_list = []

    def tambah_pengunjung(self, pengunjung):
        self.__pengunjung_list.append(pengunjung)

    def tambah_wahana(self, wahana):
        self.__wahana_list.append(wahana)

    def pesan_tiket(self, id_tiket, id_pengunjung, nama_wahana, tanggal):
        pengunjung = next((p for p in self.__pengunjung_list if p.id_pengunjung == id_pengunjung), None)
        wahana = next((w for w in self.__wahana_list if w.tampilkan_info().startswith(f"Wahana: {nama_wahana}")), None)

        if not pengunjung or not wahana:
            return "Pengunjung atau wahana tidak ditemukan."

        tiket = Tiket(id_tiket, pengunjung, wahana, tanggal)
        if tiket.validasi_tiket():
            self.__tiket_list.append(tiket)
            return "Tiket berhasil dipesan."
        else:
            return "Pengunjung tidak memenuhi batas umur untuk wahana ini."

    def tampilkan_tiket(self):
        if not self.__tiket_list:
            return "Belum ada tiket yang dipesan."
        return "\n".join(tiket.tampilkan_info() for tiket in self.__tiket_list)


# Contoh Penggunaan
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
    print(sistem.pesan_tiket("T001", "P001", "Ferris Wheel", date.today()))
    print(sistem.pesan_tiket("T002", "P001", "Roller Coaster", date.today()))
    print(sistem.pesan_tiket("T003", "P002", "Roller Coaster", date.today()))

    # Menampilkan tiket yang dipesan
    print("\nDaftar Tiket:")
    print(sistem.tampilkan_tiket())
