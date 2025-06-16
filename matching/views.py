from django.shortcuts import render
import requests


# Create your views here.
from .models import Demande,Offre
from .matching import find_nearDrivers 
def matchingPas_Drv(request,passenger_id):
    passenger = Demande.objects.get(pk=passenger_id)
    drivers = find_nearDrivers(passenger)
    return render(request,"view_matching_results.html",context={"drivers":drivers,"passenger":passenger})

def createOffre(request,driver_id):
    if request.method == "POST":
        pass
        

def createDemande(request,passenger_id):
    if request.method =="POST":
        pass
    return render(request,"demande_de_covoiturage.html")

def choicePosition(request,user_id):
    if request.method=="POST":
        latDepart = request.POST.get("start_lat")
        lngDepart = request.POST.get("start_lng")
        latArrivee = request.POST.get("end_lat")
        lngArrivee = request.POST.get("end_lng")

        latDepart,lngDepart = int(latDepart),int(lngDepart)
        url = "https://nomination.openstreetmap.org/reverse?lat={latDepart}&lon={lngDepart}&format=json"
        response = requests.get(url)
        data=response.json()
        nameDep = data.get('display_name')

        latArrivee,lngArrivee = int(latArrivee),int(lngArrivee)
        url = "https://nomination.openstreetmap.org/reverse?lat={latArrivee}&lon={lngArrivee}&format=json"
        response = requests.get(url)
        data=response.json()
        nameArr = data.get('display_name')

        if Offre.objects.get(driver__id=user_id):
            user = Offre.objects.get(driver__id=user_id)
        else:
            user = Offre.objects.get(passenger__id=user_id)
        user.departlat = latDepart
        user.departlng = lngDepart
        user.endlat = latArrivee
        user.endlng = lngArrivee

        if user.driver.conducteur:
            return render(request,"créé_une_offre_de_covoiturage.html",context={"nameDepart":nameDep,"nameArrivee":nameArr})
        return render(request,"demande_de_covoiturage.html",context={"nameDepart":nameDep,"nameArrivee":nameArr})

    return render(request,"choice_trajet.html")

    





    
