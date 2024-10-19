import requests
from datetime import datetime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from database import WeatherRecord  # Ensure correct import
from config import API_KEY, API_URL, LOCATIONS, INTERVAL, DATABASE_URI

# Set up the database session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Function to fetch weather data from the API
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

def main():
    print("Starting Weather Monitoring Application...")
    for city in LOCATIONS:
        data = fetch_weather_data(city)
        if data:
            weather_record = WeatherRecord(
                city=city,
                temperature=data['main']['temp'],
                feels_like=data['main']['feels_like'],
                main=data['weather'][0]['main'],
                timestamp=datetime.now()
            )
            session.add(weather_record)
    session.commit()
    print("Weather data fetched and stored successfully.")

if __name__ == "__main__":
    main()
