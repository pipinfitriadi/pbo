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
        print('Makanan ini bernama', self.nama, 'dibeli dengan Harga',
              self.harga, 'rupiah, termasuk dalam kategori', self.kategori)


makanan1 = Makanan("Tomat", 1500, "Vegetarian")
makanan2 = Makanan("Rendang", 17000, "Bukan Vegetarian")

print(makanan1.get_info())
print(makanan2.get_info())

print(makanan1.nama)
print(makanan1.harga)
print(makanan1.kategori)

print(makanan2.nama)
print(makanan2.harga)
print(makanan2.kategori)
