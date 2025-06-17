from django.contrib import admin
from django.urls import path, include
import views

urlpatterns = [
    path("matching <int:demande_id>/",views.matchingPas_Drv,name="matching"),
    path("create_offer <int:driver_id>",views.createOffre,name="offre"),
    path("createDemande <int:passenger_id>",views.createDemande,name="demande"),
    path("choicePosition <int:user_id>",views.choicePosition,name="takePosition"),
    path("waiting/matching <int:user_id>",views.waiting,name="waiting")
]