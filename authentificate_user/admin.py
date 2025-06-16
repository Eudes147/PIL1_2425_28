from django.contrib import admin
from .models import Utilisateur, Profil

# Register your models here.
admin.site.register(Utilisateur)
admin.site.register(Profil)