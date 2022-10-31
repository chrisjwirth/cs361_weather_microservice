import os

import requests

WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]


def lat_lon_for(city: str, state: str) -> (str, str):
    geo_api_call = (
        f"https://api.openweathermap.org/geo/1.0/direct?"
        f"q={city},{state},US&limit=1&appid={WEATHER_API_KEY}"
    )
    geo_response = requests.get(geo_api_call).json()
    return geo_response[0]["lat"], geo_response[0]["lon"]


def parsed_weather_response(weather_response: dict) -> dict:
    return {
        "weather_category": weather_response["weather"][0]["main"].title(),
        "description": weather_response["weather"][0]["description"].title(),
        "temperature": weather_response["main"]["temp"],
        "feels_like_temperature": weather_response["main"]["feels_like"],
        "temperature_minimum": weather_response["main"]["temp_min"],
        "temperature_maximum": weather_response["main"]["temp_max"],
        "humidity": weather_response["main"]["humidity"],
        "wind_speed": weather_response["wind"]["speed"],
    }
