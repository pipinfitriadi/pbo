# enkapsulasi
class Pasien:
    def __init__(self, nama, nomor_identitas, usia):
        self.__nama = nama
        self.__nomor_identitas = nomor_identitas
        self.__usia = usia
    def tampilkan_info(self):
        return f"pasien: {self.__nama}, ID: {self.__nomor_identitas}, Usia: {self.__usia}"