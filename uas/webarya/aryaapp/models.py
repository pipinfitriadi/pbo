from django.db import models

# Create your models here.
class karyaSeni(models.Model):
    Judul_Karya = models.CharField(max_length=128)
    Nama_pembuat = models.CharField(max_length=64)
    deskripsi = models.CharField(max_length=258)
    harga = models.IntegerField()

    # representasikan karyaSeni
    def __str__(self):
        return (f"ID: {self.id}: Dari {self.Judul_Karya} Dibuat oleh {self.Nama_pembuat} Deskripsi : {self.deskripsi}, dijual dengan harga Rp.{self.harga}")