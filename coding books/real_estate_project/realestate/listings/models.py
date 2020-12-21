from os import truncate
from django.db import models
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import CharField
from datetime import datetime
# from models import Realtor

# Create your models here.
class Listing(models.Model):
    realtor = models.ForeignKey('realtors.Realtor', on_delete=DO_NOTHING)
    title = models.CharField(max_length=100)
    address = models.TextField(max_length=100)
    city =models.CharField(max_length=100)
    state =models.CharField(max_length=100)
    price=models.IntegerField()
    bedrooms=models.IntegerField()
    bathrooms=models.DecimalField(max_digits=2, decimal_places=1)
    zipcode = models.CharField(max_length=10)
    garage = models.IntegerField(default=0 )
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    description = models.TextField(max_length=300, blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_2= models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

