from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Dinosaur(models.Model):
    height = models.FloatField(default=0.0)
    birth_date = models.DateTimeField('birth date')
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name + " the DINOSAUR"


class Rental(models.Model):
    rental_date = models.DateField('rental date')
    rented_dino = models.ForeignKey('Dinosaur', on_delete=models.CASCADE)
    email = models.CharField(max_length=150)

    def __str__(self):
        return str(self.rental_date)
