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
    route = GMProute(start, end)
    route.start = start
    route.end = end
    static_map = route.my_map()
    #st.write(d)
    #print(directions)
    st.image(static_map)



   
if __name__ == '__main__':
    main()