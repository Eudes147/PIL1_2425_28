from django.conf import settings
from openrouteservice import Client
from math import radians, sin, cos, sqrt, atan2

# Fonction haversine pour calculer la distance entre deux points GPS
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # rayon Terre en km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    a = sin(dlat / 2)**2 + cos(lat1)*cos(lat2)*sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c

def est_proche_trajet(route_coords, point_lat, point_lon, rayon_km=2):
    for coord in route_coords:
        route_lon, route_lat = coord
        if haversine(point_lat, point_lon, route_lat, route_lon) <= rayon_km:
            return True
    return False

def match_passager_a_conducteur(api_key, conducteur_start, conducteur_end, passager_start, passager_end):
    client = Client(key=api_key)

    route = client.directions(
        coordinates=[conducteur_start, conducteur_end],
        profile='driving-motorcycle',
        format='geojson'
    )

    route_coords = route['features'][0]['geometry']['coordinates']

    depart_ok = est_proche_trajet(route_coords, *passager_start)
    arrivee_ok = est_proche_trajet(route_coords, *passager_end)

    return depart_ok and arrivee_ok

