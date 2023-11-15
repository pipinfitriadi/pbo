#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.
class Pesawat:
    def __init__(self, nomor_keberangkatan, tujuan, waktu_keberangkatan):
        self.nomor_keberangkatan = nomor_keberangkatan
        self.tujuan = tujuan
        self.waktu_keberangkatan = waktu_keberangkatan

    def tampil_atribut(self):
        print("Nomor Keberangkatan: ", self.nomor_keberangkatan)
        print("Tujuan: ", self.tujuan)
        print("Waktu_Keberangkatan: ", self.waktu_keberangkatan) 

p1 = Pesawat("PK-123", "Jakarta", "06:00")
p1.tampil_atribut()