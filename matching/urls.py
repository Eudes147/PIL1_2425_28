from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("matching <int:demande_id>/",matchingPas_Drv,name="matching"),
    path("create_offer <int:driver_id>",createOffre,name="offre"),
    path("createDemande <int:passenger_id>",createDemande,name="demande"),
    path("choicePosition <int:user_id>",choicePosition,name="takePosition")
]