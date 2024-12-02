#  sistem manajemen portofolio investasi
class investor:
    def __init__(self, IdInvestor, nama, saldo):
        self.IdInvestor = IdInvestor
        # adanya self membuat kita bisa berinteraksi dengan data
        self.nama = nama
        self.saldo = saldo

# menampilkan info, dari investor yang ditambahkan.
    def Tampilkan_info(self):
        print(self.IdInvestor)
        print(self.nama)
        print(self.saldo)


class aset:
    def __init__(self, Id_Aset, Nama_Aset, Jenis_Aset, nilai):
        self.Id_Aset = Id_Aset
        self.Nama_Aset = Nama_Aset
        self.jenis_Aset = Jenis_Aset
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
            investor.saldo -= aset.nilai
            self.daftar_aset.append(aset)
            print(f"nama aset '{aset.Nama_Aset}' telah berhasil ditambahkan")
            print(f"di akun = '{self.investor}'")
        else:
            print("saldo tidak mencukupi untuk membeli aset.")


class SistemInfestasi:
    # berarti dalam sini akan menambahkan investor baru ke sistemnya, dimulai
    # dengan list kosong sehingga nanti diisi oleh investor baru
    def __init__(self):
        self.ListInvetor = []
        self.ListAset = []

    def tambah_investor(self, investor):
        self.ListInvetor.append(investor)
        print(f"investor '{investor.nama}' telah ditambahkan")

    def menambah_aset(self, aset):
        self.ListAset.append(aset)
        print(f"investasi '{aset.Nama_Aset}','{aset.nilai} ditambahkan")

    def kelola_portofolio(self, idinvestor, Id_portofolio):
        for investor in self.ListInvetor:
            if investor.IdInvestor == idinvestor:
                return portofolio(Id_portofolio, investor)

            print("investor tidak ditemukan")
            return None


# menggunakan sistem
sistem = SistemInfestasi()

# menambahkan investor
investor1 = investor(1, "Agus", 250000)
# memasukan pada server
sistem.tambah_investor(investor1)

aset1 = aset(1, "PtKetiduran", "saham", 100000)
sistem.menambah_aset(aset1)

portofolio1 = sistem.kelola_portofolio(1, 1)

if portofolio1:
    portofolio1.tambah_Nama_Aset(aset1)
# jikaportofolio 1 = portofolio(dibuat), maka ditambahkan tambah_aset
investor1.Tampilkan_info()
