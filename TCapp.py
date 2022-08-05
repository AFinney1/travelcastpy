from gmp_interface import *
from owm_interface import *
import streamlit as st
import datetime
import pydeck as pdk
import pandas as pd
from PIL import Image



def nearest_forecast(time, hourly_forecast):
    idx = hourly_forecast.index.get_loc(time, method='nearest')
    nearest_forecast = hourly_forecast.iloc[idx]
    #print(hourly_forecast.iloc[idx])
    return nearest_forecast

def main():
    #Get user's starting point and end point
    st.title("TravelCast" )
    start = st.text_input("Enter starting city: ", "Jackson, MS, USA")
    end = st.text_input("Enter destination city: ", "Memphis, TN, USA")

    #route initiation
    preliminary_route = GMProute(start, end)
    intermediate_locations, destination_time_deltas = preliminary_route.intermediate_coordinates()
    #Time delta calculation
    destination_time_deltas = list(map(lambda x: x.replace("mins", "min"), destination_time_deltas))
    destination_time_deltas_dt = pd.to_timedelta(destination_time_deltas) 
    time_list = []
    dt = pd.Timedelta(0)
    for j in destination_time_deltas_dt:
        dt += j
        time_list.append(dt)

    #forecast initiation and building weather list
    route_weather_list = []
    for idx, i in enumerate(intermediate_locations):
        lat = i["lat"]
        lon = i["lng"]
        forecast = WeatherForecast(lat=lat, lon=lon)
        hourly_forecast, current_forecast = forecast.get_forecast()
        # organizing the weather data
        hourly_forecast.set_index("time", inplace=True)
        #print(hourly_forecast)
        current_time = current_forecast['time'].iloc[0]

        route_forecast_times =  pd.to_datetime(pd.Series([current_time + time for time in time_list]), format = '%Y-%m-%d %H:%M:%S')
        time = route_forecast_times.iloc[idx]
        n_forecast = nearest_forecast(time, hourly_forecast)
        hourly_temp_i = n_forecast['temp']
        weather_report_i = n_forecast['weather'][0]['description']
        route_weather_list.append(weather_report_i)
        #print(hourly_temp_i, weather_report_i)
        print(weather_report_i)


    
    # print(route_forecast_times)
    # print(hourly_forecast)
    # print(nearest_time_index())
    route = GMProute(start, end, weather_list=route_weather_list)
    route.start = start
    route.end = end
    #route_points = route.my_path()[0]
    
    static_map = route.marked_map()
    #st.write(d)
    #print(directions)
    st.image(static_map)
    st.write("Weather Report Legend: C - Clear, O - clouds, R - Rain, S - Snow, T - Thunderstorm, U - Other")
    st.write("Due to constraints with Google Maps API, the markers do not support labels other than upper case letters. I will work around this in the future by substituting the labeled marker with an icon of the weather.")
  

   
if __name__ == '__main__':
    main()