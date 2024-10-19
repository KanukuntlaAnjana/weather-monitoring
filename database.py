from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

Base = declarative_base()

class WeatherRecord(Base):
    __tablename__ = 'weather_records'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    temperature = Column(Float)
    feels_like = Column(Float)
    main = Column(String)
    timestamp = Column(DateTime)

# Create the database
engine = create_engine(DATABASE_URI)
Base.metadata.create_all(engine)
