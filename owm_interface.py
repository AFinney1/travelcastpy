
import dataclasses
from dataclasses import dataclass
import requests, json
import geopy
import pandas as pd


class WeatherForecast():
    def __init__(self, city="Jackson, MS, USA", lat="32.3", lon="90.2"):
        self.city = city
        with open('OWMk.txt', 'r') as f:
            self.k = f.readlines()[0]
        self.lat = lat
        self.lon = lon
        f.close()
    def get_forecast(self):
        # try:
        k = self.k
        city = self.city
        owm_url =f"https://api.openweathermap.org/data/2.5/onecall?lat={self.lat}&lon={self.lon}&APPID={k}"
        # except:
        #     owm_url = f"https://api.openweathermap.org/data/2.5/weather?&lat={lat}&lon={lon}&APPID={key}"
        response = requests.get(owm_url)
        data = json.loads(response.content)
        #print(data)
        main = data['current']
        #print(main)
        #print(main)
       # temp = main['temp']
        #coord= data['coord']
        #lat = coord['lat']
        #lon = coord['lon']
        hourly = data['hourly']
        #print(hourly)
        weather_report = main['weather']
        #print(hourly)
        #print(weather_report)
        return pd.DataFrame(hourly)

forecast = WeatherForecast(city = "Jackson, MS, US").get_forecast()

forecast['dt'] = pd.to_datetime(forecast['dt'], unit='s')
print(forecast)