from django.db import models

# Create your models here.


class Fruits(models.Model):
    objects = None
    nomi = models.CharField(max_length=200)
    rangi = models.CharField(max_length=200)
    tami = models.CharField(max_length=200)
    price = models.IntegerField()

    def __str__(self):
        return self.nomi





