#!/usr/bin/env python3

# Copyright (c) Pipin Fitriadi. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license
# information.

from datetime import date


class Barang:
    jumlah: int
    harga_beli: float
    tanggal_kadaluwarsa: date = date(2025, 12, 31)
    harga_jual: float
    id_barang: int

    def hitung_tanggal_kadaluwarsa(self):
        pass

    def hitung_harga_jual(self):
        pass

    def hitung_diskon(self):
        pass


class DaftarTransaksi:
    data_penjualan: list
    data_pembelian: list

    def tambah_data_pejualan(self):
        pass

    def tambah_data_pembelian(self):
        pass


class DaftarStokBarang:
    barang: list
    jumlah_barang: list

    def tambah_barang(self):
        pass

    def kurang_barang(self):
        pass


class Koperasi:
    daftar_stok_barang: DaftarStokBarang
    daftar_transaksi: DaftarTransaksi

    def modifikasi_daftar_transaksi(self):
        pass
