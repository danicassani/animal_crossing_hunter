from django.db import models

# Create your models here.

class Fish(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    season_start = models.DateField()
    season_end = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Insect(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    season_start = models.DateField()
    season_end = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    

class SeaCreature(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    season_start = models.DateField()
    season_end = models.DateField()

    def __str__(self):
        return self.name
    
