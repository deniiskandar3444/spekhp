from django.contrib.auth.models import User
from django.db import models

# Create your models here.
 
class Merk(models.Model):
    nama = models.CharField(max_length=50)

    def __str__(self):
        return self.nama

    class Meta :       
        verbose_name_plural = "Merk"

class Spek(models.Model):
    nama = models.ForeignKey(User,on_delete=models.CASCADE,max_length=100, blank=True, null=True)
    produk = models.CharField(max_length=100,blank=True, null=True)
    detail = models.TextField()
    merk = models.ForeignKey(Merk, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.produk)

    class Meta:
        ordering =['-date']
        verbose_name_plural = "Spek"

class Info(models.Model):
    nomor = models.IntegerField(max_length=100,blank=True, null=True)
    nama = models.CharField(max_length=100,blank=True, null=True)
    produk = models.TextField(max_length=100,blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    detail = models.TextField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return "{} - {}".format(self.nama, self.count)
