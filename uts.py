class pesawat:

    def __init__ (self, NomorKeberangkatan, Tujuan, WaktuKeberangkatan):
        self.NomorKeberangkatan = NomorKeberangkatan
        self.Tujuan = Tujuan
        self.WaktuKeberangkatan = WaktuKeberangkatan

    def berangkat(self):
        print("Nomor Keberangkataan pesawat Ini adalah :", self.NomorKeberangkatan)

    def menuju(self):
        print("Tujuan Pesawat Ini Menuju :", self.Tujuan)

    def waktu(self):
        print("Waktu keberangkatan pesawaat ini Pukul :", self.WaktuKeberangkatan)

naikpesawat = pesawat(1, 2, 3)

naikpesawat.berangkat()
naikpesawat.menuju()
naikpesawat.waktu()
print(naikpesawat.NomorKeberangkatan, naikpesawat.Tujuan, naikpesawat.WaktuKeberangkatan)
