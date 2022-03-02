
import googlemaps
import dataclasses
from dataclasses import dataclass, field
from GMPk import gmp
import requests, json

#mport gmaps
 

@dataclass
class GMProute:
    """
    GMP Route
    """
    start: str = "Biloxi, MS"
    end: str  = "Memphis, TN"
    key : str = gmp.k
    i_start = "Biloxi, MS"
    i_end = "Memphis, TN"
    pathline : str = ""
    gmaps = googlemaps.Client(key=key)
    directions = gmaps.directions(start, end)



    def intermediate_coordinates(self) -> list:
        ic_list = []
        d = self.directions
        for doc in d[0]["legs"][0]["steps"]:
            #print(doc["end_location"])
            ic_list.append(doc["end_location"])
        return ic_list
   

    def my_path(self):
        pth = ""
        counter = 0
        center = ""
        inter_coor = self.intermediate_coordinates()
        number_of_locations = len(inter_coor)
        center_index = number_of_locations/2
        for i in inter_coor:
            counter += 1
            latlon = str(i["lat"]) + "," + str(i["lng"])
            if counter < len(inter_coor):
                pth += latlon + "|"
            else:
                pth += latlon
            if counter == center_index:
                center = latlon             
        #print(pth)
        print(center)
        return pth, center


    def my_map(self):
        key = self.key
        start = self.start
        p = self.my_path()
        path = p[0]
        path_center = p[1]
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?&center={path_center}&size=1080x1080&zoom=6&key={key}&sensor=false&mode=driving&path={path}"
        response = requests.get(map_url).content
        return response



    #start_gmaps.Geocoding(address=start)
     