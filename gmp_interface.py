
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
    pathline : str = ""
    weather_list : list = field(default_factory=list)
    gmaps = googlemaps.Client(key=key)


    def intermediate_coordinates(self):
        gmaps = self.gmaps
        start = self.start
        end = self.end
        directions = gmaps.directions(start, end)
        ic_list = []
        times = []
        d = directions
        # print(d)
        for t in d[0]["legs"][0]["steps"]:
            times.append(t["duration"]["text"])
        for doc in d[0]["legs"][0]["steps"]:
            #print(doc["end_location"])
            ic_list.append(doc["end_location"])
        return ic_list, times
    

    def my_path(self):
        pth = ""
        counter = 0
        center = ""
        inter_coor = self.intermediate_coordinates()[0]
        #print(inter_coor)
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
        #print(center)
        return pth, center



    def clean_path(self):
        path = self.my_path()[0]
        pth =  googlemaps.roads.snap_to_roads(self.gmaps, path, interpolate=True)
        counter = 0
        center = ""
        ic_list = []
        for doc in pth:
            counter += 1
            #print(doc["end_location"])
            ic_list.append(doc["location"])
        
        inter_coor = ic_list
        number_of_locations = len(inter_coor)
        center_index = number_of_locations/2
        counter = 0
        for i in inter_coor:
            counter += 1
            latlon = str(i["latitude"]) + "," + str(i["longitude"])
            if counter < len(inter_coor):
                pth += latlon + "|"
            else:
                pth += latlon
            if counter == center_index:
                center = latlon             
        #print(pth)
        #print(center)
        print(pth)
        return pth, center


    def my_map(self):
        key = self.key
        p = self.my_path()[0]
        path_center = self.my_path()[1]
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?&center={path_center}&size=1080x1080&key={key}&sensor=false&markers&mode=driving&path={p}"
        response = requests.get(map_url).content
        return response

    def marked_map(self):
        key = self.key
        p = self.my_path()[0]
        path_center = self.my_path()[1]
        markers_string = ""
        inter_coor = self.intermediate_coordinates()[0]
        for i in inter_coor:
            print(i)
        for idx, weather in enumerate(self.weather_list):
            w = weather[0].upper()
            if "clouds" in w:
                w = "O"
            if "rain" in w:
                w = "R"
            markers_string += f"&markers=color:blue%7Clabel:{w}%7C{inter_coor[idx]['lat']},{inter_coor[idx]['lng']}"
        print(markers_string)
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?&center={path_center}&size=1080x1080&key={key}&sensor=false&markers={markers_string}&mode=driving&path={p}"
        response = requests.get(map_url).content
        return response

    
    def snapped_map(self):
        key = self.key
        p = self.clean_path()[0]
        path_center = self.clean_path()[1]
        map_url = f"https://maps.googleapis.com/maps/api/staticmap?&center={path_center}&size=1080x1080&key={key}&sensor=false&mode=driving&path={p}"
        response = requests.get(map_url).content
        return response

    #start_gmaps.Geocoding(address=start)
     