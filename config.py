import os

API_KEY = "63c16f81c13c3f8be6795b421febc5dc"
API_URL = "http://api.openweathermap.org/data/2.5/weather"
DATABASE_URI = "sqlite:///weather_data.db"  # Example SQLite database URI
LOCATIONS = ["Delhi", "Mumbai", "Chennai", "Bangalore", "Kolkata", "Hyderabad"]
INTERVAL = 3600  # Fetch interval in seconds
ALERT_THRESHOLD = 35