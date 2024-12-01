#  sistem manajemen portofolio investasi
# test apakah bisa berubah langsung atau tidak pada UTSnya
class investor:
    def __init__(self, IdInvestor, nama, saldo):
        self.IdInvestor = IdInvestor
        self.nama = nama
        self.saldo = saldo

    def Tampilkan_info(self):
        print(self.IdInvestor)
        print(self.nama)
        print(self.saldo)


class asset:
    def __init__(self):
        pass


class portofolio:
    investor: str


class sistemInvestasi:
    nama: str


investor1 = investor(101, "AsepBiawak", 1000000)
investor1.Tampilkan_info()
