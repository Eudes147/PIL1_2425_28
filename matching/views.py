from django.shortcuts import render

# Create your views here.
from .models import Demande
from .matching import find_nearDrivers 
def matchingPas_Drv(request,passenger_id):
    passenger = Demande.objects.get(pk=passenger_id)
    drivers = find_nearDrivers(passenger)
    return render(request,"view_matching_results.html",context={"drivers":drivers,"passenger":passenger})