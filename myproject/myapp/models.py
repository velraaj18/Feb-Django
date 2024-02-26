from django.db import models

# Create your models here.
# class Dog:
#    name = str
#    colour = str
#    age = int

class Dog(models.Model):
   name = models.CharField(max_length=50)
   colour = models.CharField(max_length=50)
   