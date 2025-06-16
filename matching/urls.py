from django.contrib import admin
from django.urls import path
from .views import matchingPas_Drv,save_trajet

urlpatterns = [
    path("matching/<int:demande_id>/",matchingPas_Drv,name="matching"),
    path('matching/<int:demand_id',save_trajet,name="takePosition")
]