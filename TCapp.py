from gmp_interface import *
from owm_interface import *
import streamlit as st
import datetime
import pydeck as pdk
import pandas as pd
from PIL import Image



def main():
    #Get user's starting point and end point
    st.title("TravelCast" )
    start = st.text_input("Enter starting city: ", "Jackson, MS, USA")
    end = st.text_input("Enter destination city: ", "Memphis, TN, USA")

    lat = "0"
    lon = "0"
    #forecast initiation

    #route initiation
    route = GMProute(start, end)
    intermediate_locations, destination_time_deltas = route.intermediate_coordinates()

    destination_time_deltas = list(map(lambda x: x.replace("mins", "min"), destination_time_deltas))
    destination_time_deltas = pd.to_timedelta(destination_time_deltas) 
    hourly_forecast, current_forecast = WeatherForecast(city = "Jackson, MS, US").get_forecast()
    print(current_forecast)
    current_time = current_forecast['time'].iloc[0]
    time_list = []
    dt = pd.Timedelta(0)
    for i in destination_time_deltas:
        dt += i
        time_list.append(dt)
    print(time_list)
    route_forecast_times =  [current_time + time for time in time_list]
 
   # route_forecast_times =  [current_time + time for time in [sum(i,j) for j for i in destination_time_deltas]]
    print(route_forecast_times)
    route.start = start
    route.end = end
    route_points = route.my_path()[0]
    
    static_map = route.my_map()
    #st.write(d)
    #print(directions)
    st.image(static_map)
  

   
if __name__ == '__main__':
    main()