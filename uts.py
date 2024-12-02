#  sistem manajemen portofolio investasi
class investor:
    def __init__(self, IdInvestor, nama, saldo):
        self.IdInvestor = IdInvestor
        self.nama = nama
        self.saldo = saldo
# menampilkan info, dari investor yang ditambahkan.

    def Tampilkan_info(self):
        print(self.IdInvestor)
        print(self.nama)
        print(self.saldo)


class aset:
    def __init__(self, Id_Aset, Nama_Aset, Jenis_Aset, nilai):
        self.Id_Asset = Id_Aset
        self.Nama_Asset = Nama_Aset
        self.jenis_Asset = Jenis_Aset
        self.nilai = nilai

# mengubah nilai dengan nilai yang baru.
    def ubah_nilai(self, nilai_baru):
        self.nilai = nilai_baru
        print(f"nilai asset '{self.Nama_Asset}' diubah menjadi {nilai_baru}")


class portofolio:
    def __init__(self, Id_portofolio, investor):
        self.Id_portofolio = Id_portofolio
        self.investor = investor
        self.daftar_aset = []

    def tambah_aset(self, aset):
        # disini investor membeli aset, dari saldo mereka.
        # kalau saldo mereka mencukupi maka, ditambahkan aset pada portofolio
        # jika tidak tampilkan saldo tidak mencukupi
        if self.investor.saldo >= aset.nilai:
            investor.saldo - aset.nilai
            self.daftar_aset.append(aset)
            print(f"nama aset '{aset.nama_Aset}' telah berhasil ditambahkan")
            print(f"di akun = '{self.investor}'")


class SistemInfestasi:
    pass


investor1 = investor(101, "AsepBiawak", 1000000)
investor1.Tampilkan_info()
