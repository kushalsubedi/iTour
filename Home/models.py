from django.db import models
from base.models import BaseModel

# Create your models here.
 
class Places(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    slug= models.SlugField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    category_image = models.ImageField(upload_to='places', null=True, blank=True)
    def __str__(self):
        return self.name

class Package(BaseModel):
    name = models.CharField(max_length=200, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    product_image = models.ImageField(upload_to='packages', null=True, blank=True)
    category = models.ForeignKey(Places, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.name

class PackageImage(BaseModel):
    product = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='package_image', null=True, blank=True)
