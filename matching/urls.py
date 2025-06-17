from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
from .views import matchingPas_Drv
from .views import accueil_secondaire

urlpatterns = [
    path("matching/<int:demande_id>/",matchingPas_Drv,name="matching"),
    path('accueil_secondaire/', accueil_secondaire, name='accueil_secondaire'),
=======
import views

urlpatterns = [
    path("matching <int:demande_id>/",views.matchingPas_Drv,name="matching"),
    path("create_offer <int:driver_id>",views.createOffre,name="offre"),
    path("createDemande <int:passenger_id>",views.createDemande,name="demande"),
    path("choicePosition <int:user_id>",views.choicePosition,name="takePosition"),
    path("waiting/matching <int:user_id>",views.waiting,name="waiting")
>>>>>>> d73ba9b5f56f681a64c4a537b2a4ecb75beebaae
]