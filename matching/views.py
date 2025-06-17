from django.shortcuts import render
from django.shortcuts import render,redirect
from django.conf import settings
from django.core.exceptions import ValidationError

import requests


from .models import Demande,Offre
from authentificate_user.models import Profil
from .matching import match_passager_a_conducteur 

#Create views here

def waiting(request,user_name):
    passenger = request.session.get("positionPassenger")
    driver = request.session.get("positionDriver")

    if passenger:
        profil = passenger.get("passenger")
    else:
        profil = driver.get("positionDriver")
    return render(request,"matching/page_d'attente_du_matching.html",context={"profil":profil})


def matchingPas_Drv(request,passenger_name):
    demande = Demande.objects.get(passenger__user__nom = passenger_name) #Passager en question.
    offres = Offre.objects.filter(Offre.nbPlacesDispo !=0,departTime=demande.departTime)
    for offre in offres:
        if match_passager_a_conducteur(settings.API_KEY,(offre.departlng,offre.departlat),(offre.arriveelng,offre.arriveelat),(demande.departlng,demande.departlat),(demande.arriveelng,demande.arriveelat)):
            return render(request,"matching/affichage_des_resultats.html",context={"driverOffre":offre,"passengerDemande":demande})

    return render(request,"matching/affichage_des_resultats.html",context={"driverOffre":None,"passengerDemande":demande})

def createOffre(request,driver_name):
    driver = Profil.objects.get(user__nom=driver_name)
    positionDriver = request.session.get('positionDriver')
    if request.method =="POST":
        pointDepart = request.POST.get("point_depart_demande")
        pointArrivee = request.POST.get("point_arrivee_demande")
        departTime = request.POST.get("heure_depart_souhaitee")
        places = request.POST.get("places_disponibles")

        offre = Offre.objects.get(driver)
        offre.departTime = departTime
        offre.nbPlacesDispo = places
        
        try:
            offre.full_clean()
        except ValidationError as errors:
            positionDriver["erreurs"] = errors.message_dict
            return render(request,"matching/demande_de_covoiturage.html",{"positionDriver":positionDriver})
        else:
            offre.save()

            request.session["positionDriver"] = {"latDep":positionDriver.get("latDep"),"lngDep":positionDriver.get("lngDep"),"latArr":positionDriver.get("latArr"),"lngArr":positionDriver.get("lngArr"),
                "nameDepart":pointDepart,"nameArrivee":pointArrivee,"driver":driver}
            return redirect("waiting")

    return render(request,"matching/créé_une_offre_de_covoiturage.html",{"positionDriver":positionDriver,"driver":driver})
        

def createDemande(request,passenger_name):
    passenger = Profil.objects.get(user__nom=passenger_name)
    positionPassenger = request.session.get('positionPassenger')
    if request.method =="POST":
        pointDepart = request.POST.get("point_depart_demande")
        pointArrivee = request.POST.get("point_arrivee_demande")
        departTime = request.POST.get("heure_depart_souhaitee")

        demande = Demande.objects.get(passenger=passenger)
        demande.departTime = departTime

        try:
            demande.full_clean()
        except ValidationError as errors:
            positionPassenger["erreurs"] = errors.message_dict
            return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger})
        else:
            demande.save()

            request.session["positionPassenger"] = {"latDep":positionPassenger.get("latDep"),"lngDep":positionPassenger.get("lngDep"),"latArr":positionPassenger.get("latArr"),"lngArr":positionPassenger.get("lngArr"),
                "nameDepart":pointDepart,"nameArrivee":pointArrivee,"passenger":passenger}
            return redirect("waiting")


    return render(request,"matching/demande_de_covoiturage.html",{"positionPassenger":positionPassenger,"passenger":passenger})

def choicePosition(request,user_name):
    if request.method=="POST":
        latDepart = request.POST.get("start_lat")
        lngDepart = request.POST.get("start_lng")
        latArrivee = request.POST.get("end_lat")
        lngArrivee = request.POST.get("end_lng")

        latDepart,lngDepart = float(latDepart),float(lngDepart)
        url = "https://nominatim.openstreetmap.org/reverse?lat={latDepart}&lon={lngDepart}&format=json"
        response = requests.get(url)
        data=response.json()
        nameDep = f"{data['address'].get('city')}, {data['address'].get('quarter')}"


        latArrivee,lngArrivee = float(latArrivee),float(lngArrivee)
        url = "https://nominatim.openstreetmap.org/reverse?lat={latArrivee}&lon={lngArrivee}&format=json"
        response = requests.get(url)
        data=response.json()
        nameArr = f"{data['address'].get('city')}, {data['address'].get('quarter')}"
        user = Profil.objects.get(user__nom = user_name)

        if user.conducteur:
            offre = Offre(driver=user)
            offre.departlat = latDepart
            offre.departlng = lngDepart
            offre.arriveelat = latArrivee
            offre.arriveelat = lngArrivee
            offre.save()
            request.session["positionDriver"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
            return redirect('offre')
        
        demande = Demande(passenger=user)
        demande.departlat = latDepart
        demande.departlng = lngDepart
        demande.arriveelat = latArrivee
        demande.arriveelat = lngArrivee
        demande.save()
        request.session["positionPassenger"] = {"latDep":latDepart,"lngDep":lngDepart,"latArr":latArrivee,"lngArr":lngArrivee,
                "nameDepart":nameDep,"nameArrivee":nameArr}
        return redirect('demande')

    return render(request,"matching/choice_trajet.html",{"user":user})


def accueil_secondaire(request):
    return render(request, "matching/page_accueil_secondaire.html")
