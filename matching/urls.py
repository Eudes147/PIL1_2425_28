from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("matching",matchingPas_Drv,name="matching"),
    path("create_offer",createOffre,name="offre"),
    path("<str:nameUser>/createDemande",createDemande,name="demande"),
    path("choicePosition",choicePosition,name="takePosition"),
    path("<str:nameUser>/resultMatching",matchingPas_Drv,name="results"),
    path("<str:nameUser>/accueil-secondaire",accueil_secondaire,name="accueil_secondaire")
]
