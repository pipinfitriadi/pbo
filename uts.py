class RambuLaluLintas:
    def __init__(self, warna_rambu):
        self.warna_rambu = warna_rambu

    def info_rambu(self):
        print(f"Rambu lalu lintas ini berwarna {self.warna_rambu}.")

    def ubah_warna(self, warna_baru):
        self.warna_rambu = warna_baru
        print(f"Warna rambu lalu lintas telah diubah menjadi {self.warna_rambu}.")


rambu1 = RambuLaluLintas('Merah')
rambu1.info_rambu()

rambu1.ubah_warna('Kuning')
rambu1.info_rambu()
