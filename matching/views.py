from django.shortcuts import render

# Create your views here.
from .models import Demande
from .matching import find_nearDrivers 

def save_trajet(request):
    if request.method=='POST':
        latDepart = request.POST.get("start_lat")
        lngDepart = request.POST.get("start_lng")
        latArrivee = request.POST.get("end_lat")
        lngArrivee = request.POST.get("end_lng")
        context = {"start_lat":latDepart,
                   'start_lng':lngDepart,
                   'end_lat':latArrivee,
                   'end_lng':lngArrivee}
        return render(request,"créé_une_offre_de_covoiturage.html",context)



def matchingPas_Drv(request,passenger_id):
    passenger = Demande.objects.get(pk=passenger_id)
    drivers = find_nearDrivers(passenger)
    return render(request,"view_matching_results.html",context={"drivers":drivers,"passenger":passenger})