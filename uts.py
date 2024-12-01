#  sistem manajemen portofolio investasi
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
    def __init__(self, Id_Asset, Nama_Asset, Jenis_Asset, nilai):
        self.Id_Asset = Id_Asset
        self.Nama_Asset = Nama_Asset
        self.jenis_Asset = Jenis_Asset
        self.nilai = nilai

    def ubah_nilai(self, nilai_baru):
        self.nilai = nilai_baru
        print(f"nilai asset '{self.Nama_Asset}' diubah menjadi {nilai_baru}")


class portofolio:
    def __init__(self, Id_portofolio, investor, daftar_asset):
        self.Id_portofolio = Id_portofolio

investor1 = investor(101, "AsepBiawak", 1000000)
investor1.Tampilkan_info()
