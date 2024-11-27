class Pelangganan:
    def __innit__(self, nama, nomor_identitas, umur):
        self.nama = nama
        self.nomor_identitas = nomor_identitas
        self.umur = umur
    def tampilkan_info(self):
        return f"Pelanggan: {self.nama}, ID: {self.nomor_identitas}, Umur: {self.umur} tahun"

class Kendaraan:
    def __innit__(self, nomor_polisi, tipe, harga_per_hari):
        self.nomor_polisi = nomor_polisi
        self.tipe = tipe
        self.harga_per_hari = harga_per_hari
        self.status = "tersedia"

    def ubah_status(self, status):
        self.status = status

    def tampilkan_info(self):
        return f"Kendaraan: {self.tipe}, No Polisi: {self.nomor_polisi}, Harga: Rp{self.harga_per_hari}/hari, Status: {self.status}"

