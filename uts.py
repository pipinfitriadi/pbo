#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
class Karyawan:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji

    def ubah_gaji(self, gaji_baru):
        self.gaji = gaji_baru
        print(f"Gaji { self.nama} berhasil diubah menjadi {self.gaji}")


karyawan1 = Karyawan("Sumanto", "Staff", 3000000)
print(f"Gaji awal Sumanto adalah {karyawan1.gaji}")

karyawan1.ubah_gaji(4000000)
print(f"Gaji baru Sumanto adalah {karyawan1.gaji}")
