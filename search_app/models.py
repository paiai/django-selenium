from django.db import models

# Create your models here.
class Category(models.Model):
    cate_num = models.IntegerField()
    cate_name = models.CharField(max_length=50)

class Place(models.Model):
    cate = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    lat = models.CharField(max_length=10)
    lon = models.CharField(max_length=10)
    tel = models.CharField(max_length=20)