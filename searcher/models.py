from django.db import models
from .constants import FISH_LOCATIONS, INSECT_LOCATIONS

# Create your models here.

class Fish(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField(default="No description available.")
    price = models.IntegerField(default=0)
    season_start = models.DateField(null=True, blank=True)
    season_end = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, choices=FISH_LOCATIONS)

    def __str__(self):
        return self.name


class Insect(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField(default="No description available.")
    price = models.IntegerField(default=0)
    season_start = models.DateField(null=True, blank=True)
    season_end = models.DateField(null=True, blank=True)
    location = models.CharField(max_length=200, choices=INSECT_LOCATIONS)

    def __str__(self):
        return self.name
    

class SeaCreature(models.Model):
    name = models.CharField(max_length=200)
    image_path = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    price = models.IntegerField(default=0)
    season_start = models.DateField(null=True, blank=True)
    season_end = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name
    
