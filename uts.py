# Kelas Karyawan
class Karyawan:
    def __init__(self, id_karyawan, nama, posisi):
        self.__id_karyawan = id_karyawan  # Atribut privat
        self.__nama = nama
        self.__posisi = posisi

    def get_id(self):
        return self.__id_karyawan

    def get_nama(self):
        return self.__nama

    def get_posisi(self):
        return self.__posisi

    def tampilkan_info(self):
        # Polimorfisme diterapkan di sini
        return f"Karyawan [ID: {self.__id_karyawan}, Nama: {self.__nama}, Posisi: {self.__posisi}]"


# Kelas Proyek
class Proyek:
    def __init__(self, nama_proyek, deskripsi, deadline):
        self.__nama_proyek = nama_proyek  # Atribut privat
        self.__deskripsi = deskripsi
        self.__deadline = deadline
        self.__karyawan = []  # Daftar karyawan dalam proyek

    def get_nama_proyek(self):
        return self.__nama_proyek

    def tambahkan_karyawan(self, karyawan):
        self.__karyawan.append(karyawan)

    def tampilkan_info(self):
        # Polimorfisme diterapkan di sini
        info_karyawan = "\n".join([k.tampilkan_info() for k in self.__karyawan])
        return (f"Proyek [Nama: {self.__nama_proyek}, Deskripsi: {self.__deskripsi}, "
                f"Deadline: {self.__deadline}]\nKaryawan Terlibat:\n{info_karyawan}")


# Kelas Tugas
class Tugas:
    def __init__(self, id_tugas, deskripsi, proyek, status="Belum Selesai"):
        self.__id_tugas = id_tugas  # Atribut privat
        self.__deskripsi = deskripsi
        self.__proyek = proyek
        self.__status = status

    def ubah_status(self, status_baru):
        self.__status = status_baru

    def tampilkan_info(self):
        # Polimorfisme diterapkan di sini
        return (f"Tugas [ID: {self.__id_tugas}, Deskripsi: {self.__deskripsi}, "
                f"Proyek: {self.__proyek.get_nama_proyek()}, Status: {self.__status}]")


# Kelas SistemManajemenProyek
class SistemManajemenProyek:
    def __init__(self):
        self.__proyek_list = []  # Daftar proyek
        self.__tugas_list = []  # Daftar tugas
        self.__karyawan_list = []  # Daftar karyawan

    def tambahkan_karyawan(self, karyawan):
        self.__karyawan_list.append(karyawan)

    def tambahkan_proyek(self, proyek):
        self.__proyek_list.append(proyek)

    def tambahkan_tugas(self, tugas):
        self.__tugas_list.append(tugas)

    def tampilkan_semua_proyek(self):
        return "\n\n".join([proyek.tampilkan_info() for proyek in self.__proyek_list])

    def tampilkan_semua_tugas(self):
        return "\n".join([tugas.tampilkan_info() for tugas in self.__tugas_list])


# Contoh Penggunaan Sistem
if __name__ == "__main__":
    # Membuat beberapa karyawan
    k1 = Karyawan(1, "Danur", "Developer")
    k2 = Karyawan(2, "Cahya", "Designer")

    # Membuat proyek
    proyek1 = Proyek("Website", "Mengubah desain website", "2024-12-31")
    proyek1.tambahkan_karyawan(k1)
    proyek1.tambahkan_karyawan(k2)

    # Membuat tugas
    tugas1 = Tugas(101, "implementasi kode website", proyek1)
    tugas2 = Tugas(102, "desain website", proyek1)
    tugas2.ubah_status("Selesai")

    # Sistem Manajemen Proyek
    sistem = SistemManajemenProyek()
    sistem.tambahkan_karyawan(k1)
    sistem.tambahkan_karyawan(k2)
    sistem.tambahkan_proyek(proyek1)
    sistem.tambahkan_tugas(tugas1)
    sistem.tambahkan_tugas(tugas2)

    # Menampilkan semua proyek dan tugas
    print("=== Semua Proyek ===")
    print(sistem.tampilkan_semua_proyek())

    print("\n=== Semua Tugas ===")
    print(sistem.tampilkan_semua_tugas())
