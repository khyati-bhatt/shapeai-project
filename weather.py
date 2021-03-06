import requests
from datetime import datetime
api_key='5701733791dc744672e25018128821c4'
location=input("Enter the city name:: ")
comp_apilink='https://api.openweathermap.org/data/2.5/weather?q='+location+'&appid='+api_key
api_link=requests.get(comp_apilink)
api_data=api_link.json()

temp=((api_data['main']['temp'])-273.15)
weather_desc=api_data['weather'][0]['description']
humidity=api_data['main']['humidity']
wind_spd=api_data['wind']['speed']
date_time=datetime.now().strftime('%d %b %Y | %I:%M:%S %p')
print('--------------------------------------------------------')
print("Weather Stats for- {} || {}".format(location.upper(), date_time))
print('--------------------------------------------------------')
print('Current temperature is     :{:.2f} deg C'.format(temp))
print("Current weather description:",weather_desc)
print("Current humidity           :",humidity,'%')
print("Current wind speed         :",wind_spd,'kmph')
