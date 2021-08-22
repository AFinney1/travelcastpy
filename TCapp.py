from gmp_interface import *
from owm_interface import *
import streamlit as st
import pydeck as pdk




def main():
    st.title("TravelCast")
    start = st.text_input("Enter starting city: ", "Biloxi, MS, USA")
    end = st.text_input("Enter destination city: ", "Memphis, TN, USA")
    #owm ->lat lon-> gmp - directions> TCapp.py
    #owm -weather -> gmp - directions> TCapp.py
    forecast = owm()
    start_coordinates = (forecast.lat, forecast.lon)
    end_coordinates = (forecast.lat, forecast.lon)
    route = GMProute(start = start_coordinates, end = end_coordinates)
    directions = route.response.text
    print(directions)
    col1 = st. columns(1)
    col1.image(directions)
    return None

   
if __name__ == '__main__':
    main()