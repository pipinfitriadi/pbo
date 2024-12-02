class Pekerja:
    def __init__(self, id_pekerja, nama, posisi, gaji_per_jam):
        self.__id_pekerja = id_pekerja
        self.__nama = nama
        self.__posisi = posisi
        self.__gaji_per_jam = gaji_per_jam

    def hitung_gaji(self, jam_kerja):
        return self.__gaji_per_jam * jam_kerja

    def __str__(self):
        return f"{self.__nama} (ID: {self.__id_pekerja}, Posisi: {self.__posisi})"


class Proyek:
    def __init__(self, nama_proyek, lokasi, deadline):
        self.__nama_proyek = nama_proyek
        self.__lokasi = lokasi
        self.__deadline = deadline
        self.__pekerja = []

    def tambahkan_pekerja(self, pekerja):
        self.__pekerja.append(pekerja)

    def get_pekerja(self):
        return self.__pekerja

    def __str__(self):
        return f"Proyek: {self.__nama_proyek}, Lokasi: {self.__lokasi}, Deadline: {self.__deadline}"


class Tugas:
    def __init__(self, id_tugas, deskripsi, proyek):
        self.__id_tugas = id_tugas
        self.__deskripsi = deskripsi
        self.__status = "Belum Dimulai"
        self.__proyek = proyek

    def ubah_status(self, status_baru):
        self.__status = status_baru

    def get_status(self):
        return self.__status

    def __str__(self):
        return f"Tugas ID: {self.__id_tugas}, Deskripsi: {self.__deskripsi}, Status: {self.__status}"


class SistemManajemenKonstruksi:
    def __init__(self):
        self.__proyek_list = []
        self.__pekerja_list = []

    def tambah_proyek(self, proyek):
        self.__proyek_list.append(proyek)

    def tambah_pekerja(self, pekerja):
        self.__pekerja_list.append(pekerja)

    def kelola_tugas(self, id_tugas, deskripsi, proyek, pekerja):
        if pekerja in proyek.get_pekerja():
            tugas = Tugas(id_tugas, deskripsi, proyek)
            return tugas
        else:
            raise ValueError("Pekerja tidak terdaftar di proyek ini.")

    def __str__(self):
        return f"Sistem Manajemen Konstruksi dengan {len(self.__proyek_list)} proyek dan {len(self.__pekerja_list)} pekerja."



if __name__ == "__main__":
    # Membuat sistem manajemen konstruksi
    sistem = SistemManajemenKonstruksi()

    # Menambahkan pekerja
    pekerja1 = Pekerja(1, "Tantra", "manajer proyek", 100000)
    pekerja2 = Pekerja(2, "Zaid", "Mandor", 20000)
    sistem.tambah_pekerja(pekerja1)
    sistem.tambah_pekerja(pekerja2)

    # Menambahkan proyek
    proyek1 = Proyek("Proyek pembangunan praktisi", "Bandung", "2024-11-31")
    proyek1.tambahkan_pekerja(pekerja1)
    proyek1.tambahkan_pekerja(pekerja2)
    sistem.tambah_proyek(proyek1)

   
    try:
        tugas1 = sistem.kelola_tugas(1, "Mengawasi pekerja dan proyek", proyek1, pekerja1)
        print(tugas1)
        tugas1.ubah_status("Sedang Dikerjakan")
        print(tugas1)
    except ValueError as e:
        print(e)

    try:
        tugas2 = sistem.kelola_tugas(2, "Menyelesaikan konstruksi di lapangan", proyek1, pekerja2)
        print(tugas2)
        tugas2.ubah_status("Sedang Dikerjakan")
        print(tugas2)
    except ValueError as e:
        print(e)

    # Menghitung gaji pekerja
    jam_kerja = 5
    print(f"Gaji {pekerja1}: {pekerja1.hitung_gaji(jam_kerja)}")
    print(f"Gaji {pekerja2}: {pekerja2.hitung_gaji(jam_kerja)}")

