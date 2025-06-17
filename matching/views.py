from django.shortcuts import render
from .models import Demande
from .matching import find_nearDrivers 



def matchingPas_Drv(request,passenger_id):
    passenger = Demande.objects.get(pk=passenger_id)
    drivers = find_nearDrivers(passenger)
    return render(request,"view_matching_results.html",context={"drivers":drivers,"passenger":passenger})





def accueil_secondaire(request):
    return render(request, "matching/page_accueil_secondaire.html")