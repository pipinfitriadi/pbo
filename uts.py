import math


class Lingkaran:

    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        return math.pi * self.jari_jari ** 2

    def hitung_keliling(self):
        return 2 * math.pi * self.jari_jari


# Contoh penggunaan
jari_jari_lingkaran = float(input("Masukkan jari-jari lingkaran: "))
lingkaran = Lingkaran(jari_jari_lingkaran)

luas = lingkaran.hitung_luas()
keliling = lingkaran.hitung_keliling()

print(f"Luas lingkaran: {luas:.2f}")
print(f"Keliling lingkaran: {keliling:.2f}")
