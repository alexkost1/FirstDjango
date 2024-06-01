from django.db import models

# Create your models here.
class Color(models.Model):
   name = models.CharField(max_length=32)
   
class Item(models.Model):
   name  = models.CharField(max_length=100)
   brand = models.CharField(max_length=100)
   count = models.PositiveIntegerField()
   description =  models.CharField(max_length=100, default = '')
   colors = models.ManyToManyField(to=Color)


