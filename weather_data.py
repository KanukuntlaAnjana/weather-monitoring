import requests
from config import API_KEY, API_URL

def fetch_weather_data(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # To get temperature in Celsius
    }

    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to fetch data for {city}")
        return None

