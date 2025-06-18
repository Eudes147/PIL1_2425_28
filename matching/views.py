from django.shortcuts import render
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db.models import Q

import requests

from .models import Demande,Offre
from authentificate_user.models import Profil
from .matching import match_passager_a_conducteur

#Create views here

def matchingPas_Drv(request,nameUser):
    positionPassenger = request.session.get("positionUser")
    demande = Demande.objects.filter(passenger__user__username = nameUser).last() #Passager en question.
    offres = Offre.objects.filter(~Q(nbPlacesDispo=0),departTime=demande.departTime)
    for offre in offres:
        if match_passager_a_conducteur(settings.API_KEY,(offre.departlng,offre.departlat),(offre.arriveelng,offre.arriveelat),(demande.departlng,demande.departlat),(demande.arriveelng,demande.arriveelat)):
            return render(request,"matching/affichage_des_resultats.html",context={"driverOffre":offre,"passengerDemande":demande})

    return render(request,"matching/affichage_des_resultats.html",context={"driverOffre":None,"passengerDemande":demande,"positionUser":positionPassenger})

def createOffre(request,nameUser=None):
    driver = Profil.objects.get(user__id=request.user.id)
    print(driver.user.username)
    #driver.user.username = request.user.username
    positionDriver = request.session.get('positionDriver')
    if request.method =="POST":
        print(driver.user.username)
        pointDepart = request.POST.get("point_depart_demande")
        pointArrivee = request.POST.get("point_arrivee_demande")
        departTime = request.POST.get("heure_depart")
        places = int(request.POST.get("places_disponibles"))

        offre = Offre.objects.filter(driver=driver).last()
        offre.departTime = departTime
        offre.nbPlacesDispo = places
        
        try:
            offre.full_clean()
            offre.save()
            print("Cherche")
        except ValidationError as errors:
            positionDriver["erreurs"] = errors.message_dict
            print(errors.message_dict)
            return render(request,"matching/créé_une_offre_de_covoiturage.html",{"positionDriver":positionDriver})
        else:
            print("Save")

            request.session["positionDriver"] = {"latDep":positionDriver.get("latDep"),"lngDep":positionDriver.get("lngDep"),"latArr":positionDriver.get("latArr"),"lngArr":positionDriver.get("lngArr"),
                "nameDepart":pointDepart,"nameArrivee":pointArrivee,"driver_id": driver.id,"driver_name": driver.user.username}
            return redirect("chat")
        

    return render(request,"matching/créé_une_offre_de_covoiturage.html",{"positionDriver":positionDriver,"driver":driver})
        

def createDemande(request,nameUser=None):
    passenger = Profil.objects.get(user__id=request.user.id)
    print(passenger.user.username)
    positionPassenger = request.session.get('positionPassenger')
    if request.method =="POST":
        pointDepart = request.POST.get("point_depart_demande")
        pointArrivee = request.POST.get("point_arrivee_demande")
        departTime = request.POST.get("heure_depart_souhaitee")

        demande = Demande.objects.filter(passenger=passenger).last()

        demande.departTime = departTime

        try:
            demande.full_clean()
            demande.save()
        except ValidationError as errors:
            positionPassenger["erreurs"] = errors.message_dict
            return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger})
        else:
            request.session["positionPassenger"] = {"latDep":positionPassenger.get("latDep"),"lngDep":positionPassenger.get("lngDep"),"latArr":positionPassenger.get("latArr"),"lngArr":positionPassenger.get("lngArr"),
                "nameDepart":pointDepart,"nameArrivee":pointArrivee,"passenger_id": passenger.id, "passenger_name": passenger.user.username}
            return redirect("results", nameUser=nameUser)

    return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger,"passenger":passenger})

def choicePosition(request,nameUser=None):
    user = Profil.objects.get(user__id=request.user.id)
    print(user.user.username)
    if request.method=="POST":
        latDepart = request.POST.get("start_lat")
        lngDepart = request.POST.get("start_lng")
        latArrivee = request.POST.get("end_lat")
        lngArrivee = request.POST.get("end_lng")

        latDepart,lngDepart = float(latDepart),float(lngDepart)
        url = f"https://nominatim.openstreetmap.org/reverse?lat={latDepart}&lon={lngDepart}&format=json"
        response = requests.get(url, headers={"User-Agent": "DjangoApp"})
        data=response.json()
        addressDep = data.get("address")
        ville = (
            addressDep.get("city")
            or addressDep.get("town")
            or addressDep.get("village")
            or addressDep.get("hamlet")
            or addressDep.get("county")  # si aucun des précédents
        )

        quartier = (
            addressDep.get("suburb")
            or addressDep.get("neighbourhood")
            or addressDep.get("quarter")
            or addressDep.get("residential")
            or addressDep.get("locality")
        )
        nameDep = f"{ville}, {quartier}"

        print(f"latDepart: {latDepart}, lngDepart: {lngDepart}, nameDep: {nameDep}")    
        latArrivee,lngArrivee = float(latArrivee),float(lngArrivee)
        url = f"https://nominatim.openstreetmap.org/reverse?lat={latArrivee}&lon={lngArrivee}&format=json"
        response = requests.get(url, headers={"User-Agent": "DjangoApp"})
        data=response.json()
        addressArr = data.get("address")
        print(f"latArrivee: {latArrivee}, lngArrivee: {lngArrivee}")
        ville = (
            addressArr.get("city")
            or addressArr.get("town")
            or addressArr.get("village")
            or addressArr.get("hamlet")
            or addressArr.get("county")  # si aucun des précédents
        )

        quartier = (
            addressArr.get("suburb")
            or addressArr.get("neighbourhood")
            or addressArr.get("quarter")
            or addressArr.get("residential")
            or addressArr.get("locality")
        )
        nameArr = f"{ville}, {quartier}"

        print(f"latArrivee: {latArrivee}, lngArrivee: {lngArrivee}")
        print(f"nameArrivee: {nameArr}")
        user = Profil.objects.get(user__id=request.user.id)
        print(user.user.username)
        print(user.conducteur)
        if user.conducteur==True:
            offre = Offre(driver=user)
            offre.departlat = latDepart
            offre.departlng = lngDepart
            offre.arriveelat = latArrivee
            offre.arriveelng = lngArrivee
            offre.save()
            request.session["positionDriver"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
            return redirect("offre")
        demande = Demande(passenger=user)
        demande.departlat = latDepart
        demande.departlng = lngDepart
        demande.arriveelat = latArrivee
        demande.arriveelng = lngArrivee
        demande.save()
        request.session["positionPassenger"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
        return redirect("demande", nameUser=nameUser)

    return render(request,"matching/choice_trajet.html",{"user":user})


def accueil_secondaire(request,nameUser):
    profil = Profil.objects.get(user__username=nameUser)
    return render(request, "matching/page_accueil_secondaire.html",{"conducteur":profil.conducteur,"profil":profil})
