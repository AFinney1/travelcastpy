
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
    start: str 
    end: str  
    key : str = gmp.k
    i_start = "Biloxi, MS"
    i_end = "Memphis, TN"
    pathline : str = ""
    gmaps = googlemaps.Client(key=key)
    directions = gmaps.directions(i_start, i_end)

    def __post_init__(self):
        if self.start is None:
            self.start : str = self.i_start
        if self.end is None:
            self.end : str = self.i_end

    def intermediate_coordinates(d) -> list:
        ic_list = []
        for doc in d[0]["legs"][0]["steps"]:
            #print(doc["end_location"])
            ic_list.append(doc["end_location"])
        return ic_list
    
    inter_coor = intermediate_coordinates(directions)

    def my_path(inter_coor):
        pth = ""
        counter = 0
        center = ""
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

    path = my_path(inter_coor)
    def my_map(self):
        key = self.key
        start = self.start
        p = self.path[0]
        path_center = self.path[1]
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?&center={path_center}&size=1080x1080&zoom=6&key={key}&sensor=false&mode=driving&path={p}"
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
     