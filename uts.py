
class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, Umur: {self.umur} tahun")



class Instruktur(Orang):
    def __init__(self, nama, umur, spesialisasi, jadwal):
        super().__init__(nama, umur)
        self.spesialisasi = spesialisasi
        self.jadwal = jadwal

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Spesialisasi: {self.spesialisasi}")
        print(f"Jadwal: {', '.join(self.jadwal)}")



class Murid(Orang):
    def __init__(self, nama, umur, tingkat):
        super().__init__(nama, umur)
        self.tingkat = tingkat
        self.kelas = None

    def daftar_kelas(self, kelas):
        self.kelas = kelas
        kelas.tambah_murid(self)
        print(f"{self.nama} telah mendaftar ke kelas {kelas.nama_kelas}.")

    def tampilkan_info(self):
        super().tampilkan_info()
        print(f"Tingkat: {self.tingkat}")
        if self.kelas:
            print(f"Terdaftar di kelas: {self.kelas.nama_kelas}")
        else:
            print("Belum terdaftar di kelas manapun.")



class KelasMusik:
    def __init__(self, nama_kelas, instruktur, jadwal):
        self.nama_kelas = nama_kelas
        self.instruktur = instruktur
        self.jadwal = jadwal
        self.murid = []

    def tampilkan_info(self):
        print(f"Kelas: {self.nama_kelas}")
        print(f"Instruktur: {self.instruktur.nama}")
        print(f"Jadwal: {', '.join(self.jadwal)}")
        print(f"Murid terdaftar: {len(self.murid)}")
        if self.murid:
            print("Murid-murid:")
            for murid in self.murid:
                print(f"- {murid.nama} ({murid.tingkat})")
        else:
            print("Belum ada murid yang terdaftar.")

    def tambah_murid(self, murid):
        self.murid.append(murid)


class SistemSekolahMusik:
    def __init__(self):
        self.murid_list = []
        self.instruktur_list = []
        self.kelas_list = []

    def tambah_murid(self, murid):
        self.murid_list.append(murid)
        print(f"Murid {murid.nama} berhasil ditambahkan.")

    def tambah_instruktur(self, instruktur):
        self.instruktur_list.append(instruktur)
        print(f"Instruktur {instruktur.nama} berhasil ditambahkan.")

    def tambah_kelas(self, kelas):
        self.kelas_list.append(kelas)
        print(f"Kelas {kelas.nama_kelas} berhasil ditambahkan.")

    def tampilkan_info_sistem(self):
        print("\nInformasi Sekolah Musik:")
        print("\nInstruktur:")
        for instruktur in self.instruktur_list:
            instruktur.tampilkan_info()
            print()

        print("\nMurid:")
        for murid in self.murid_list:
            murid.tampilkan_info()
            print()

        print("\nKelas Musik:")
        for kelas in self.kelas_list:
            kelas.tampilkan_info()
            print()



if __name__ == "__main__":
    
    sistem = SistemSekolahMusik()

   
    instruktur_1 = Instruktur("Muhamad hazbi", 35, "Piano", ["Senin 10:00", "Rabu 10:00"])
    instruktur_2 = Instruktur("imam gazali", 28, "Gitar", ["Selasa 14:00", "Kamis 14:00"])

   
    sistem.tambah_instruktur(instruktur_1)
    sistem.tambah_instruktur(instruktur_2)

   
    kelas_piano = KelasMusik("Kelas Piano", instruktur_1, ["Senin 10:00", "Rabu 10:00"])
    kelas_gitar = KelasMusik("Kelas Gitar", instruktur_2, ["Selasa 14:00", "Kamis 14:00"])

   
    sistem.tambah_kelas(kelas_piano)
    sistem.tambah_kelas(kelas_gitar)

   
    murid_1 = Murid("John Doe", 18, "Pemula")
    murid_2 = Murid("Jane Smith", 22, "Menengah")

    
    sistem.tambah_murid(murid_1)
    sistem.tambah_murid(murid_2)

   
    murid_1.daftar_kelas(kelas_piano)
    murid_2.daftar_kelas(kelas_gitar)

    
    sistem.tampilkan_info_sistem()
