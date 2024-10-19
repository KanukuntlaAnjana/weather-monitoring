import matplotlib.pyplot as plt
from database import WeatherRecord
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

def visualize_data():
    records = session.query(WeatherRecord).all()
    cities = [record.city for record in records]
    temperatures = [record.temperature for record in records]
    
    plt.bar(cities, temperatures)
    plt.xlabel("City")
    plt.ylabel("Temperature (°C)")
    plt.title("Weather Data Visualization")
    plt.show()
