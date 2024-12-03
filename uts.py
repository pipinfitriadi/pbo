class peserta:
    """kelas untuk mempresentasikan peserta event."""
    def __init__ (self, id_peserta, nama, jenis_tiket):
        self.id_peserta = id_peserta
        self.nama =  nama
        self.jenis_tiket = jenis_tiket

    def tampilkan _info(self):
        """menampilkan informasi peserta."""
        return f"ID peserta: {self.id_peserta}, nama: {self.nama}, jenis tiket: {self.jenis_tiket}"


class event:
    """kelas untuk mempresentasikan sebuah event."""
    def __init__(self, nama_event, lokasi, tanggal):
        self.nama_event = nama_event
        self.lokasi = lokasi
        self.tanggal = tanggal

    def tampilkan_info(self):
        """menampilkan informasi event"""
        return f"event: {self.nama_event}, lokasi: {self.lokasi}, tanggal: {self.tanggal}"


class kegiatan:
    """kelas untuk mempresentasikan kegiatan dalam event."""
    def __init__(self, id_kegiatan, nama_kegiatan, jadwal, event):
        self.id_kegiatan = id_kegiatan
        self.nama_kegiatan = nama_kegiatan
        self.jadwal = jadwal
        self.event = event

    def ubah_jadwal(self, jadwal_baru):
        """mengubah jadwal kegiatan"""
        self.jadwal = jadwal_baru
        return f"jadwal kegiatan '{self.nama_kegiatan}' telah diubah menjadi {self.jadwal}"


class sistemevent:
    """kelas untuk mengelola peserta, event, dan kegiatan."""
    def__init__(self):
        self.peserta = []
        self.event = []
        self.kegiatan = []

    def tambah_peserta(self, peserta):
        """menambahkan peserta ke dalam event."""
        self.peserta.append(peserta)
        return f"peserta {peserta.nama} berhasil ditambahkan."

    def tambah_event(self, event):
        """menambahkan event ke dalam sistem."""
        self.event.append(event)
        return f"peserta '{event.nama_event}' berhasil ditambahkan."

    def tambah_kegiatan(self, kegiatan):
        """  menambahkan kegiatan ke dalam sistem. memastikan tidak ada jadwal yang bertabrakan dalam event yang sama."""
        for  keg in self.kegiatan:
            if keg.event.nama_event == kegiatan.event.nama_event and keg.jadwal == kegiatan.jadwal:
                return f"jadwal kegiatan '{kegiatan.nama_kegiatan}' .bertabrakan dengan '{keg.nama_kegiatan}'."
        self.kegiatan.append(kegiatan)
        return f"kegiatan '{kegiatan.nama_kegiatan}' berhasil ditambahkan."

    def tampilkan_info_kegiatan(self)
    """menampilkan informasi semua kegiatan dalam sistem."""
    return [f"{keg.nama_kegiatan} ({keg.jadwal}) - event: {keg.event.nama_event}" for keg in self.kegiatan]


if__name__ == "__main__":
    peserta1 = peserta(1, "Indah", "VIP")
    peserta2 = peserta(2, "Laras", "Regular")

    event1 = event("Pensi", "Bandung", "2024-12-17")

    sistem = sistemevent()
    print(sistem.tambah_event(event1))
    print(sistem.tambah_peserta(peserta1))
    print(sistem.tambah_peserta(peserta2))

    kegiatan1 = kegiatan(101, "workshop", "09.00-11.00", event1)
    kegiatan2 = kegiatan(102, "konser", "11.00-15,00", event2)

    print(sistem.tambah_kegiatan(kegiatan1))
    print(sistem.tambah_kegiatan(kegiatan2))

    print("\peserta:")
    for p in sistem.peserta:
        print(p.tampilkan_info())

    print("\event")
    for e in sistem.event:
        print(e.tampilkan_info)

    print("\kegiatan")
    for k in sistem.tampilkan_info_kegiatan():
        print(k)