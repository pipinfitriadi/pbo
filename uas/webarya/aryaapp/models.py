from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Customers
class Customer(models.Model):
    Nama_depan = models.CharField(max_length=50)
    Nama_belakang = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    pasword = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.Nama_depan} {self.Nama_belakang}'
    
# Product
class karyaSeni(models.Model):
    Judul_Karya = models.CharField(max_length=128)
    image = models.ImageField(upload_to='uploads/images/', null=True, blank=True)  # Allow null and blank
    Nama_pembuat = models.CharField(max_length=64)
    Category = models.ForeignKey(Category, default=1, on_delete=models.CASCADE)
    deskripsi = models.CharField(max_length=258, default='', blank=True, null=True)
    harga = models.DecimalField(default=0, max_digits=5, decimal_places=2)

    def __str__(self):
        return (f"ID: {self.id}: Dari {self.Judul_Karya} Dibuat oleh {self.Nama_pembuat} Deskripsi : {self.deskripsi}, dijual dengan harga Rp.{self.harga}")
    
# Customer order
class Order(models.Model):
    product = models.ForeignKey(karyaSeni, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    addres = models.CharField(max_length=50, default='', blank=True)
    phone = models.CharField(max_length=20, default='', blank=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product
