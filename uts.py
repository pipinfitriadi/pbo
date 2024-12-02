class Siswa:
    def __init__(self, id_siswa, nama, email):
        self.id_siswa = id_siswa
        self.nama = nama
        self.email = email

    def tampilkan_info(self):
        return f"ID Siswa: {self.id_siswa}"
        return f"Nama: {self.nama}"
        return f"Email: {self.email}"

class Instruktur:
    def __init__(self, id_instruktur, nama, keahlian):
        self.id_instruktur = id_instruktur
        self.nama = nama
        self.keahlian = keahlian

    def tampilkan_info(self):
        return f"ID Instruktur: {self.id_instruktur}"
        return f"Nama: {self.nama}"
        return f"Keahlian: {self.keahlian}"

class Kursus:
    def __init__(self, id_kursus, nama_kursus, deskripsi, instruktur, kapasitas_max):
        self.id_kursus = id_kursus
        self.nama_kursus = nama_kursus
        self.deskripsi = deskripsi
        self.instruktur = instruktur
        self.kapasitas_max = kapasitas_max
        self.siswa_terdaftar = []

    def tambah_siswa(self, siswa):
        if len(self.siswa_terdaftar) < self.kapasitas_max:
            self.siswa_terdaftar.append(siswa)
            print(f"Siswa {siswa.nama} berhasil terdaftar di kursus {self.nama_kursus}.")
        else:
            print(f"Maaf kursus {self.nama_kursus} sudah memenuhi kapasitas. Tidak dapat menambah siswa {siswa.nama}.")

    def tampilkan_info(self):
        instruktur_info = self.instruktur.tampilkan_info()
        return f"ID Kursus: {self.id_kursus}"
        return f"Nama: {self.nama_kursus}"
        return f"Deskripsi: {self.deskripsi}"
        return f"Instruktur: {instruktur_info}"
        return f"Jumlah Pendaftar: {len(self.siswa_terdaftar)}/{self.kapasitas_max}"

class SistemKursus:
    def __init__(self):
        self.siswa_list = []
        self.instruktur_list = []
        self.kursus_list = []

    def tambah_siswa(self, id_siswa, nama, email):
        siswa = Siswa(id_siswa, nama, email)
        self.siswa_list.append(siswa)
        print(f"Siswa {nama} berhasil ditambahkan.")

    def tambah_instruktur(self, id_instruktur, nama, keahlian):
        instruktur = Instruktur(id_instruktur, nama, keahlian)
        self.instruktur_list.append(instruktur)
        print(f"Instruktur {nama} berhasil ditambahkan.")

    def tambah_kursus(self, id_kursus, nama_kursus, deskripsi, id_instruktur, kapasitas_max):
        instruktur = next((i for i in self.instruktur_list if i.id_instruktur == id_instruktur), None)
        if instruktur:
            kursus = Kursus(id_kursus, nama_kursus, deskripsi, instruktur, kapasitas_max)
            self.kursus_list.append(kursus)
            print(f"Kursus {nama_kursus} berhasil ditambahkan.")
        else:
            print(f"Instruktur dengan ID {id_instruktur} tidak ditemukan.")

    def daftar_kursus(self):
        for kursus in self.kursus_list:
            print(kursus.tampilkan_info())

    def daftar_siswa_per_kursus(self, id_kursus):
        kursus = next((k for k in self.kursus_list if k.id_kursus == id_kursus), None)
        if kursus:
            print(f"Siswa yang terdaftar di kursus {kursus.nama_kursus}:")
            for siswa in kursus.siswa_terdaftar:
                print(f"- {siswa.nama}")
        else:
            print(f"Kursus dengan ID {id_kursus} tidak ditemukan.")

    def pendaftaran_siswa_ke_kursus(self, id_siswa, id_kursus):
        siswa = next((s for s in self.siswa_list if s.id_siswa == id_siswa), None)
        kursus = next((k for k in self.kursus_list if k.id_kursus == id_kursus), None)
        
        if siswa and kursus:
            kursus.tambah_siswa(siswa)
        else:
            if not siswa:
                print(f"Siswa dengan ID {id_siswa} tidak ditemukan.")
            if not kursus:
                print(f"Kursus dengan ID {id_kursus} tidak ditemukan.")


sistem = SistemKursus()

sistem.tambah_siswa(1, "Ali", "ali@mail.com")
sistem.tambah_siswa(2, "Sinta", "sinta@mail.com")
sistem.tambah_siswa(3, "Andi", "andi@mail.com")
print("----------------------------")
sistem.tambah_instruktur(1, "Rudy", "Pemrograman")
sistem.tambah_instruktur(2, "Siti", "Pemrograman Web")
print("----------------------------")
sistem.tambah_kursus(1, "Pemrograman", "Kursus untuk belajar Pemograman", 1, 3)
sistem.tambah_kursus(2, "Pemrograman Web", "Kursus untuk belajar Web", 2, 2)
print("----------------------------")
sistem.pendaftaran_siswa_ke_kursus(1, 1)
sistem.pendaftaran_siswa_ke_kursus(2, 1)
sistem.pendaftaran_siswa_ke_kursus(3, 1)
sistem.pendaftaran_siswa_ke_kursus(1, 2)
print("----------------------------")
sistem.daftar_kursus()

sistem.daftar_siswa_per_kursus(1)
sistem.daftar_siswa_per_kursus(2)