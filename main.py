import os

import requests
from fastapi import FastAPI

from utils import lat_lon_for, parsed_weather_response

app = FastAPI()

WEATHER_API_KEY = os.environ["WEATHER_API_KEY"]


@app.get("/")
async def root():
    instructions = (
        "Welcome to the Weather Microservice! "
        "To get the current weather, visit '/weather/', "
        "and pass a U.S. city and state as query parameters."
    )
    example = "http://127.0.0.1:8000/weather/?city=Denver&state=Colorado"
    return {"instructions": instructions, "example": example}


@app.get("/weather/")
async def say_hello(city: str, state: str) -> dict:
    lat, lon = lat_lon_for(city, state)
    weather_api_call = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&units=imperial&appid={WEATHER_API_KEY}"
    )
    weather_response = requests.get(weather_api_call).json()
    return parsed_weather_response(weather_response)
