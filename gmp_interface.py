
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
    start: str = "Biloxi,MS,USA"
    end: str = "Memphis,MS,USA"
    gmaps = googlemaps.Client(key=key)
    directions = gmaps.directions(start, end)

    def my_map(self):
        key = self.key
        start = self.start
        path = self.directions
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={start}&size=720x720&zoom=13&key={key}"
        response = requests.get(map_url).content
        return response

    def inter_locations(self):
        """
        Return a list of locations between the start and end locations
        """
        start = self.start
        end = self.end
        distance_matrix = self.gmaps.distance_matrix(self.start, self.end)
        return distance_matrix
    #start_gmaps.Geocoding(address=start)
     