from django.db import models
from django.shortcuts import timezone

# Create your models here.
class Offre(models.Model):
    driver = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # Position de départ du conducteur (latitude, longitude).
    departlatitude = models.CharField(max_length=200)
    departlongitude = models.CharField(max_length=200)

    # Position d'arrivée du conducteur (latitude, longitude).
    arriveelatitude = models.CharField(max_length=200)
    arriveelongitude = models.CharField(max_length=200)

    #Heure de départ
    departTime = models.TimeField(default=timezone.now)

    #Nombre de places disponibles
    nbPLacesDispo = models.PositiveIntergerField(default=driver.nbplaces)


class Demande(models.Model):
    passenger = models.ForeignKey(User,on_delete=models.CASCADE)
    
    # Position de départ du conducteur (latitude, longitude).
    departlatitude = models.CharField(max_length=200)
    departlongitude = models.CharField(max_length=200)

    # Position d'arrivée du conducteur (latitude, longitude).
    arriveelatitude = models.CharField(max_length=200)
    arriveelongitude = models.CharField(max_length=200)

    #Heure de départ
    departTime = models.TimeField(timezone.now)




