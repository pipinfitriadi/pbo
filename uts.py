class Produk:
    def __init__(self, id_produk, nama, kategori, harga, stok):
        self.__id_produk = id_produk
        self.__nama = nama
        self.__kategori = kategori
        self.__harga = harga
        self.__stok = stok

    # Metode untuk menampilkan informasi produk
    def tampilkan_info(self):
        info = f"ID: {self.__id_produk}, Nama: {self.__nama}, Kategori: {self.__kategori}, Harga: {self.__harga}, Stok: {self.__stok}"
        return info

    # Getter untuk stok
    def get_stok(self):
        return self.__stok

    # Setter untuk stok
    def set_stok(self, stok):
        self.__stok = stok