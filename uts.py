class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def hitung_luas(self):
        luas = 3.14 * self.jari_jari**2
        return luas

    def hitung_keliling(self):
        keliling = 2 * 3.14 * self.jari_jari
        return keliling


jari_jari_lingkaran = 10
lingkaran_saya = Lingkaran(jari_jari_lingkaran)

luas_lingkaran = lingkaran_saya.hitung_luas()
keliling_lingkaran = lingkaran_saya.hitung_keliling()

print("Luas lingkaran: ", luas_lingkaran)
print("Keliling lingkaran: ", keliling_lingkaran)
