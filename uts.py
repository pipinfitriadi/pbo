#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

class Kendaraan:
    def __init__(self, maksimal_kecepatan, jarak_tempuh):
        self.maksimal_kecepatan = maksimal_kecepatan
        self.jarak_tempuh = jarak_tempuh

    def info_kendaraan(self):
        print(f"Maksimal kecepatan {self.maksimal_kecepatan} km/jam ")
        print(f"Jarak tempuh {self.jarak_tempuh} km.")

    def ubah_kecepatan(self, kecepatan_baru):
        self.maksimal_kecepatan = kecepatan_baru
        print(f"Maksimal kecepatan menjadi {self.maksimal_kecepatan} km/jam.")

    def tambah_jarak(self, jarak_tambahan):
        self.jarak_tempuh += jarak_tambahan
        print(f"Jarak tempuh bertambah menjadi {self.jarak_tempuh} km.")


# Contoh penggunaan class Kendaraan
mobil = Kendaraan(200, 50000)
mobil.info_kendaraan()

mobil.ubah_kecepatan(220)
mobil.tambah_jarak(100)
mobil.info_kendaraan()
