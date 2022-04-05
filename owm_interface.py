
import dataclasses
from dataclasses import dataclass
import requests, json

import pandas as pd


class WeatherForecast():

    def __init__(self, city="Jackson, MS, USA", lat="32.3", lon="90.2"):
        self.city = city
        self.lat = lat
        self.lon = lon
        with open('OWMk.txt', 'r') as f:
            self.k = f.readlines()[0]
        f.close()

    def city_to_geocoordinates(self):
        city = self.city
        k = self.k
        geocode = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={k}"
        response = requests.get(geocode)
        geo_data = json.loads(response.content)
        #print(geo_data)
        self.lat = geo_data[0]['lat']
        self.lon = geo_data[0]['lon']
        return self.lat, self.lon
       
    def get_forecast(self):
        # try:
        k = self.k
        owm_url =f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&APPID={k}"
        # except:
        #     owm_url = f"https://api.openweathermap.org/data/2.5/weather?&lat={lat}&lon={lon}&APPID={key}"
        response = requests.get(owm_url)
        data = json.loads(response.content)
        main = data['current']
        hourly = data['hourly']
        weather_report = main['weather']
        hourly_df = pd.DataFrame(hourly)
        hourly_df['dt'] = pd.to_datetime(hourly_df['dt'], unit='s')
        hourly_df.rename(columns={'dt':'time'}, inplace=True)
        main_df = pd.DataFrame(main)
        main_df['dt'] = pd.to_datetime(main_df['dt'], unit='s')
        main_df.rename(columns={'dt':'time'}, inplace=True)
        return hourly_df, main_df


