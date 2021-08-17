from gmp_interface import *
from owm_interface import *
import streamlit as st
import pydeck as pdk




def main():
    st.title("TravelCast")
    start = st.text_input("Enter starting city: ")
    end = st.text_input("Enter destination city: ")
    #owm ->lat lon-> gmp - directions> TCapp.py
    #owm -weather -> gmp - directions> TCapp.py
    forecast = owm()
    dist_matrix = gmp(lat = forecast.lat, lon = owm.lon).gmp_url
    route1 = GMProute(start = start, end = end)
     
    print(dist_matrix)
    st.beta_columns(dist_matrix)
    return None

   
if __name__ == '__main__':
    main()