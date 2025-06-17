from django.db import models
from django.utils import timezone
from authentificate_user.models import Profil

# Create your models here.
class Offre(models.Model):
    driver = models.ForeignKey(Profil,on_delete=models.CASCADE)
    # Position de départ du conducteur (latitude, longitude).
    departlat = models.FloatField()
    departlng = models.FloatField()

    # Position d'arrivée du conducteur (latitude, longitude).
    arriveelat = models.FloatField()
    arriveelng = models.FloatField()

    #Heure de départ
    departTime = models.TimeField(default=timezone.now)

    #Nombre de places disponibles
    nbPLacesDispo = models.PositiveIntegerField(default=1)


class Demande(models.Model):
    passenger = models.ForeignKey(Profil,on_delete=models.CASCADE)
    
    # Position de départ du conducteur (latitude, longitude).
    departlat = models.FloatField(max_length=200)
    departlng= models.FloatField(max_length=200)

    # Position d'arrivée du conducteur (latitude, longitude).
    arriveelat = models.FloatField(max_length=200)
    arriveelng = models.FloatField(max_length=200)

    #Heure de départ
    departTime = models.TimeField(timezone.now)




