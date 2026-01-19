import datetime as dt
import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = os.getenv("OPENWEATHER_API_KEY")
CITY = "New York"


def kelvin_to_celsius_farenheit(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return celsius, farenheit

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

temp_kelvin = response["main"]["temp"]
temp_celsius, temp_farenheit = kelvin_to_celsius_farenheit(temp_kelvin)
feels_like_kelvin = response["main"]["feels_like"]
feels_like_celsius, feels_like_farenheit = kelvin_to_celsius_farenheit(feels_like_kelvin)
wind_speed = response["wind"]["speed"]
humidity = response["main"]["humidity"]
description = response["weather"][0]["description"]
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], tz=dt.UTC)
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], tz=dt.UTC)


print(f"Temperature in {CITY}: {temp_celsius:.2f}ºC or {temp_farenheit}ºF")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}ºC or {feels_like_farenheit}ºF")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {wind_speed}m/s")
print(f"General Weather in {CITY}: {description}")
print(f"Sunrises in {CITY} at {sunrise_time} local time.")
print(f"Sunsets in {CITY}: at {sunset_time} local time.")



