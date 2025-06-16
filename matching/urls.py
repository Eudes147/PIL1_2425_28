from django.contrib import admin
from django.urls import path, include
from .views import matchingPas_Drv

urlpatterns = [
    path("matching/<int:demande_id>/",matchingPas_Drv,name="matching"),
]