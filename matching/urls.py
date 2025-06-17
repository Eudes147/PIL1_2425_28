from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("matching",matchingPas_Drv,name="matching"),
    path("create_offer",createOffre,name="offre"),
    path("createDemande",createDemande,name="demande"),
    path("choicePosition",choicePosition,name="takePosition"),
    path("waiting",waiting,name="waiting"),
    path("resultMatching",matchingPas_Drv,name="results"),
]
