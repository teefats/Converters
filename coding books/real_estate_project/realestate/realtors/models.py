from os import name
from django.db import models
from django.db.models.fields import DateField
from datetime import datetime
# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(max_length=600, blank=True)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length= 50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.now, blank=True)
    
    def __str__(self):
            return self.name



# class Contact(models.Model):
#     name = models.CharField(max_length=200)
#     photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
#     description = models.TextField(max_length=600)
#     email = models.EmailField(max_length = 100)
#     phone = models.PhoneNumberField(_(""))
#     is_mvp = models.BooleanField(default=True)
#     hire_date = models.DateField()
    
#     class Meta:
#         verbose_name = _("")
#         verbose_name_plural = _("s")

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse("_detail", kwargs={"pk": self.pk})
# )