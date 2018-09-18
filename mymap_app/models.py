from django.db import models

class MapData(models.Model):
    title = models.CharField(max_length=200),
    lat = models.CharField(max_length=50),
    lon = models.CharField(max_length=50),
    flag = models.IntegerField(default=0),
    link = models.URLField()

    def __str__(self):
    	return self.title