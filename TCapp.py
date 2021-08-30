from gmp_interface import *
from owm_interface import *
import streamlit as st
import pydeck as pdk
from PIL import Image



def main():
    #Get user's starting point and end point
    st.title("TravelCast" )
    start = st.text_input("Enter starting city: ", "Jackson, MS, USA")
    end = st.text_input("Enter destination city: ", "Memphis, TN, USA")


    #forecast initiation
    forecast = owm()
    start_coordinates = (forecast.lat, forecast.lon)
    end_coordinates = (forecast.lat, forecast.lon)

    #route initiation
    route = GMProute()
    route.start = start
    route.end = end
    directions = route.my_map()
    path = route.inter_locations()
    #print(path)
    d = route.directions
    st.write(d)
    #print(directions)
    st.image(directions)
    for doc in d[0]["legs"][0]["steps"]:
        print(doc["end_location"])
    return None

   
if __name__ == '__main__':
    main()