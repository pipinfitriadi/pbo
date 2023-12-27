#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

class Film:
    def __init__(self, judul, sutradara, jumlah_penonton):
        self.judul = judul
        self.sutradara = sutradara
        self.jumlah_penonton = jumlah_penonton

    def ubah_jumlah_penonton(self, jumlah_penonton_baru):
        self.jumlah_penonton = jumlah_penonton_baru


film = Film("Dilan 1990", "Fajar Bustomi", 1000000)

print(film.judul)
# Dilan 1990

print(film.sutradara)
# Fajar Bustomi

print(film.jumlah_penonton)
# 1000000

film.ubah_jumlah_penonton(2000000)

print(film.jumlah_penonton)
# 2000000
