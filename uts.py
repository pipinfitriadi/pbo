#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

class Makanan:
    def __init__(self, nama, harga, kategori):
        self.nama = nama
        self.harga = harga
        self.kategori = kategori

    def get_info(self):
        print(
            f"Makanan ini bernama {self.nama}",
            f"dibeli dengan harga {self.harga}",
            f"dan termasuk kedalam {self.kategori}")
        print()
        print(f"Nama: {self.nama}")
        print(f"Harga: {self.harga}")
        print(f"Kategori: {self.kategori}")
        print()


makanan1 = Makanan("Tomat", 1500, "Vegetarian")
makanan2 = Makanan("Rendang", 17000, "Bukan Vegetarian")

makanan1.get_info()
makanan2.get_info()
