from OWMk import k
import dataclasses
from dataclasses import dataclass
import requests, json



@dataclass
class owm():
    key = k.key
    city = "Biloxi,ms,us"
    owm_url =f"https://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
    response = requests.get(owm_url)
    data = json.loads(response.content)
    main = data['main']
    temp = main['temp']
    coord= data['coord']
    lat = coord['lat']
    lon = coord['lon']
    weather_report = data['weather']

