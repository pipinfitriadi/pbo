class rambulalulintas:
    def __init__(self, warna):
        self.warna = warna

    def tampilkan_inpo(self):
        print(f"Warna rambu lalu lintas adalah {self.warna}")

    def ubah_warna(self, warna_baru):
        self.warna = warna_baru
        print(f"Warna rambu lalu lintas berhasil diubah menjadi {self.warna}")


if __name__ == "__main__":
    rambu = rambulalulintas('Merah')

    rambu.tampilkan_inpo()

    rambu.ubah_warna('Kuning')

    rambu.tampilkan_inpo()

    rambu.ubah_warna('hijau')

    rambu.tampilkan_inpo()
