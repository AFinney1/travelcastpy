from gmp_interface import *
from owm_interface import *
import streamlit as st
import pydeck as pdk
from PIL import Image



def main():
    st.title("TravelCast" )
    start = st.text_input("Enter starting city: ", "Jackson, MS, USA")
    end = st.text_input("Enter destination city: ", "Memphis, TN, USA")
    #owm ->lat lon-> gmp - directions> TCapp.py
    #owm -weather -> gmp - directions> TCapp.py
    forecast = owm()
    start_coordinates = (forecast.lat, forecast.lon)
    end_coordinates = (forecast.lat, forecast.lon)
    route = GMProute()
    route.start = start
    route.end = end
    directions = route.my_map()
    #print(directions)
    st.image(directions)
    return None

   
if __name__ == '__main__':
    main()