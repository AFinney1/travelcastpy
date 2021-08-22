
import googlemaps
import dataclasses
from dataclasses import dataclass
from GMPk import gmp
import requests, json

#mport gmaps
 

@dataclass
class GMProute:
    """
    GMP Route
    """
    key : str = gmp.k
    start: str = "Biloxi, MS, USA"
    end: str = "Memphis, MS, USA"
    gmaps = googlemaps.Client(key=key)
    directions = gmaps.directions(start, end)
    map_url = f"https://maps.googleapis.com/maps/api/staticmap?center=Jackson,MS&zoom=13&size=600x300&maptype=roadmap&markers=color:blue4&key={key}"
    response = requests.get(map_url)
    
    #start_gmaps.Geocoding(address=start)
     