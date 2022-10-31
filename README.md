# Weather Microservice

## Introduction
Welcome to the Weather Microservice by Chris Wirth! This service takes a U.S. 
city and state as query parameters and returns the current weather conditions.

## Installation and Initialization
1. Clone the repository.
2. Run `python -m pip install -r requirements.txt`.
3. Export the environment variable `WEATHER_API_KEY`, set to your [Open Weather 
Map](https://openweathermap.org/) API key.
4. Run the program.
5. Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your 
browser.

## Communication Contract

### Requesting Data
To request weather data, visit [http://127.0.0.1:8000/weather/](http://127.0.0.1:8000/weather/) 
and pass a 
U.S. city and state as query parameters. 

#### Sample Request
[http://127.0.0.1:8000/weather/?city=Denver&state=Colorado]("http://127.0.0.1:8000/weather/?city=Denver&state=Colorado")

### Receiving Data
After processing your request, the service will return the following weather 
information for the provided U.S. city/state.
- Weather Category
- Description
- Temperature
- Feels Like Temperature
- Temperature Minimum
- Temperature Maximum
- Humidity
- Wind Speed

#### Sample Response
```json
{
    "category": "Clouds",
    "description": "Scattered Clouds",
    "temperature": 45.88,
    "feels_like_temperature": 45.88,
    "temperature_minimum": 39.18,
    "temperature_maximum": 49.91,
    "humidity": 36,
    "wind_speed": 0.6
}
```

### UML Sequence Diagram
![UML Sequence Diagram](https://user-images.githubusercontent.com/82831529/198924404-92bb4817-5672-430a-ab4b-45a420d42574.png)
