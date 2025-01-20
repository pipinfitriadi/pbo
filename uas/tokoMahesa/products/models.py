from django.db import models
from djangoo.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=true)
    
    
    class Meta:
        varbose_name_plural = "categories"
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.Foreginkey(Category. related_name='products', on_delete=models.CASCADE) 
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='/products', blank=True, null=True)
    
    def __str__(self) -> str:
        return self.name
    
    def def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'id':self.id, 'siug':self.slug})
    
    
    
