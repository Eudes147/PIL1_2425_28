from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, unique=True)
    Role = models.CharField(max_length=15) 
    password = models.CharField(max_length=25)
    pass

class Profil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    depart_lat = models.FloatField(blank=True, null=True)
    depart_lng = models.FloatField(blank=True, null=True)
    heure_depart = models.TimeField(blank=True, null=True)
    heure_arrivee = models.TimeField(blank=True, null=True)
    conducteur = models.BooleanField(default=False)
    marque = models.CharField(max_length=100, blank=True)
    modele = models.CharField(max_length=100, blank=True)
    places = models.PositiveIntegerField(blank=True, null=True)

