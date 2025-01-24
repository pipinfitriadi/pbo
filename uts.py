# Kelas Induk
class Person:
    def __init__(self, id_person, nama):
        self.id_person = id_person
        self.nama = nama

    def tampilkan_info(self):
        raise NotImplementedError("Metode ini harus diimplementasikan di kelas turunan.")


# Kelas Karyawan, turunan dari Person
class Karyawan(Person):
    def __init__(self, id_karyawan, nama, departemen):
        super().__init__(id_karyawan, nama)
        self.departemen = departemen

    def tampilkan_info(self):
        print(f"Karyawan ID: {self.id_person}")
        print(f"Nama: {self.nama}")
        print(f"Departemen: {self.departemen}")
        print("-" * 30)


# Kelas Instruktur, turunan dari Person
class Instruktur(Person):
    def __init__(self, id_instruktur, nama, keahlian):
        super().__init__(id_instruktur, nama)
        self.keahlian = keahlian

    def tampilkan_info(self):
        print(f"Instruktur ID: {self.id_person}")
        print(f"Nama: {self.nama}")
        print(f"Keahlian: {', '.join(self.keahlian)}")
        print("-" * 30)


# Kelas Pelatihan
class Pelatihan:
    def __init__(self, id_pelatihan, nama_pelatihan, deskripsi, instruktur):
        self.id_pelatihan = id_pelatihan
        self.nama_pelatihan = nama_pelatihan
        self.deskripsi = deskripsi
        self.instruktur = instruktur

    def tampilkan_info(self):
        print(f"Pelatihan ID: {self.id_pelatihan}")
        print(f"Nama Pelatihan: {self.nama_pelatihan}")
        print(f"Deskripsi: {self.deskripsi}")
        print(f"Instruktur: {self.instruktur.nama}")
        print("-" * 30)


# Kelas SistemPelatihan
class SistemPelatihan:
    def __init__(self):
        self.karyawan = []
        self.pelatihan = []

    def tambah_karyawan(self, karyawan):
        self.karyawan.append(karyawan)
        print(f"Karyawan {karyawan.nama} berhasil ditambahkan.")

    def tambah_pelatihan(self, pelatihan):
        self.pelatihan.append(pelatihan)
        print(f"Pelatihan {pelatihan.nama_pelatihan} berhasil ditambahkan.")

    def daftar_karyawan_ke_pelatihan(self, id_karyawan, id_pelatihan):
        karyawan = next((k for k in self.karyawan if k.id_person == id_karyawan), None)
        pelatihan = next((p for p in self.pelatihan if p.id_pelatihan == id_pelatihan), None)

        if not karyawan:
            print("Karyawan tidak ditemukan.")
            return
        if not pelatihan:
            print("Pelatihan tidak ditemukan.")
            return

        if karyawan.departemen.lower() in pelatihan.deskripsi.lower():
            print(f"Karyawan {karyawan.nama} berhasil didaftarkan ke pelatihan {pelatihan.nama_pelatihan}.")
        else:
            print(f"Karyawan {karyawan.nama} tidak dapat mendaftar ke pelatihan {pelatihan.nama_pelatihan} karena tidak relevan dengan departemennya.")

    def tampilkan_data(self):
        print("\nDaftar Karyawan:")
        for k in self.karyawan:
            k.tampilkan_info()

        print("Daftar Pelatihan:")
        for p in self.pelatihan:
            p.tampilkan_info()


# Contoh Penggunaan Sistem
if __name__ == "__main__":
    # Membuat objek instruktur
    instruktur1 = Instruktur(1, "Pak pipin", ["Programming", "pemograman berorientasi objek"])
    instruktur2 = Instruktur(2, "Pak ponsen", ["Marketing", "Branding","copywriting"])

    # Membuat objek pelatihan
    pelatihan1 = Pelatihan(1, "Python Programming", "programming", instruktur1)
    pelatihan2 = Pelatihan(2, "Digital Marketing", "marketing", instruktur2)

    # Membuat objek karyawan
    karyawan1 = Karyawan(1, "Novi", "Programming")
    karyawan2 = Karyawan(2, "Miftah", "Marketing")
    karyawan3 = Karyawan(3, "Hanif", "Finance")

    # Membuat sistem pelatihan
    sistem = SistemPelatihan()

    # Menambahkan data
    sistem.tambah_karyawan(karyawan1)
    sistem.tambah_karyawan(karyawan2)
    sistem.tambah_karyawan(karyawan3)

    sistem.tambah_pelatihan(pelatihan1)
    sistem.tambah_pelatihan(pelatihan2)

    # Mendaftarkan karyawan ke pelatihan
    sistem.daftar_karyawan_ke_pelatihan(1, 1)  # Berhasil
    sistem.daftar_karyawan_ke_pelatihan(2, 1)  # Gagal
    sistem.daftar_karyawan_ke_pelatihan(3, 2)  # Gagal

    # Menampilkan data
    sistem.tampilkan_data()
