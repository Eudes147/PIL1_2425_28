import math

from .models import Offre

def haversine(latPas,longPas,latDrv,longDrv):
    rayonEarth = 6371
    phi1, phi2 = math.radians(latPas), math.radians(latDrv)
    dphi = math.radians(latDrv-latPas)
    dlambda = math.radians(longDrv-longPas)
    a = math.sin(dphi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(dlambda/2)**2
    c = 2*math.atan(math.sqrt(a))

    return rayonEarth * c

def find_nearDrivers(passenger,rayonSearch=15):
    drivers = Offre.objects.filter(
        departTime = passenger.departTime
    )
    results=[]
    for driver in drivers:
        distance = haversine(passenger.departlatitude,
                             passenger.departlongitude,
                             driver.departlatitude,
                             driver.departlongitude)
        if distance <=rayonSearch:
            results.append((driver,round(distance,2)))
    
    results.sort(key=lambda comp: comp[1])
    return results