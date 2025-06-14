from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=15, unique=True)
    Role = models.CharField(max_length=15) , 
    password = models.CharField(max_length=25)
    pass



