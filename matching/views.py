from django.shortcuts import render,redirect
from django.conf import settings
from django.core.exceptions import ValidationError

import requests


from .models import Demande,Offre
from .matching import match_passager_a_conducteur 

#Create views here
def waiting(request,user_id):
    positionPassenger = request.session.get('positionPassenger')
    
    return render(request,"matching/page_d'attente_du_matching.html")
def matchingPas_Drv(request,passenger_id):
    passenger = Demande.objects.get(pk=passenger_id) #Passager en question.
    drivers = Offre.objects.get(Offre.nbPlacesDispo !=0,departTime=passenger.departTime)
    for driver in drivers:
        if match_passager_a_conducteur(settings.API_KEY,(driver.departlng,driver.departlat),(driver.arriveelng,driver.arriveelat),(passenger.departlng,passenger.departlat),(passenger.arriveelng,passenger.arriveelat)):
            return render(request,"matching/affichage_des_resultats.html",context={"driver":driver,"passenger":passenger})

    return render(request,"matching/affichage_des_resultats.html",context={"driver":None,"passenger":passenger})
def createOffre(request,driver_id):
    if request.method == "POST":
        pass

    return render(request,"matching/créé_une_offre_de_covoiturage.html")
        

def createDemande(request,passenger_id):
    positionPassenger = request.session.get('positionPassenger')
    if request.method =="POST":
        pointDepart = request.POST.get("point_depart_demande")
        pointArrivee = request.POST.get("point_arrivee_demande")
        departTime = request.POST.get("heure_depart_souhaitee")

        demande = Demande(passenger=Demande.objects.get(pk=passenger_id),
                                         departlat=positionPassenger.get("latDep"),
                                         departlng=positionPassenger.get("lngDep"),
                                         arriveelat=positionPassenger.get("latArr"),
                                         arriveelng=positionPassenger.get("lngArr"),
                                         departTime=positionPassenger.get('departTime'))
        
        try:
            demande.full_clean()
        except ValidationError as errors:
            positionPassenger["erreurs"] = errors.message_dict
            return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger})
        else:
            demande.save()

            request.session["positionPassenger"] = {"latDep":positionPassenger.get("latDep"),"lngDep":positionPassenger.get("lngDep"),"latArr":positionPassenger.get("latArr"),"lngArr":positionPassenger.get("lngArr"),
                "nameDepart":positionPassenger.get("nameDep"),"nameArrivee":positionPassenger.get("nameArr")}
            return redirect("waiting")


    return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger})

def choicePosition(request,user_id):
    if request.method=="POST":
        latDepart = request.POST.get("start_lat")
        lngDepart = request.POST.get("start_lng")
        latArrivee = request.POST.get("end_lat")
        lngArrivee = request.POST.get("end_lng")

        latDepart,lngDepart = float(latDepart),float(lngDepart)
        url = "https://nominatim.openstreetmap.org/reverse?lat={latDepart}&lon={lngDepart}&format=json"
        response = requests.get(url)
        data=response.json()
        nameDep = f"{data["address"].get("city")}, {data["address"].get("quarter")}"

        latArrivee,lngArrivee = float(latArrivee),float(lngArrivee)
        url = "https://nominatim.openstreetmap.org/reverse?lat={latArrivee}&lon={lngArrivee}&format=json"
        response = requests.get(url)
        data=response.json()
        nameArr = f"{data["address"].get("city")}, {data["address"].get("quarter")}"

        if Offre.objects.get(driver__id=user_id):
            user = Offre.objects.get(driver__id=user_id)
        else:
            user = Offre.objects.get(passenger__id=user_id)
        user.departlat = latDepart
        user.departlng = lngDepart
        user.endlat = latArrivee
        user.endlng = lngArrivee

        if user.driver.conducteur:
            request.session["positionDriver"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
            return redirect('offre')
        request.session["positionPassenger"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
        return redirect('demande')

    return render(request,"matching/choice_trajet.html")

    





    
