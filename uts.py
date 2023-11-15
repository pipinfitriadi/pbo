class Pelajar:
    def __init__(self, nama):
        self.nama = nama
        self.kelas = []

    def tampilkan_kelas(self):
        print(f"Pelajar {self.nama} sedang mengikuti kelas:")
        for kelas in self.kelas:
            print(f"- {kelas}")

    def tambahkan_kelas(self, kelas):
        self.kelas.append(kelas)


siswa = Pelajar("Feri Ahmad")
siswa.tambahkan_kelas("Pemograman Berorientasi Objek")
siswa.tambahkan_kelas("Arsitektur Komputer")
siswa.tampilkan_kelas()
# Output: Pelajar Adi sedang mengikuti kelas:
# - Matematika
# - Bahasa Indonesia
