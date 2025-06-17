from django.contrib import admin
from django.urls import path, include
from .views import matchingPas_Drv
from .views import accueil_secondaire

urlpatterns = [
    path("matching/<int:demande_id>/",matchingPas_Drv,name="matching"),
    path('accueil_secondaire/', accueil_secondaire, name='accueil_secondaire'),
]