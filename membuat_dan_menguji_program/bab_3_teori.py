#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

from datetime import date


class Barang:
    jumlah: int  # Ini komentar
    harga_beli: int
    tanggal_kadaluwarsa: date
    harga_jual: int
    id_barang: str
    diskon: float = 0.0

    def set_harga_beli(self, harga_beli: int):
        self.harga_beli = harga_beli


class MataKuliah:
    nilai: str

    def set_nilai(self, uas: float, uts: float, quiz: float, tugas: float):
        nilai = (uas * 0.4 + uts * 0.4 + quiz * 0.1 + tugas * 0.1)/4

        if nilai <= 80:
            self.nilai = "E"
        else:
            self.nilai = "D"


laptop = Barang()
mobil_listrik = Barang()

print(laptop.diskon)
laptop.harga_beli = 1000
print(laptop.harga_beli)

mobil_listrik.diskon = 5.3
print(mobil_listrik.diskon)
mobil_listrik.set_harga_beli(3500)
print(mobil_listrik.harga_beli)
