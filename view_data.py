from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import WeatherRecord, DATABASE_URI

# Set up the database session
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

# Fetch all records from the database
records = session.query(WeatherRecord).all()

# Display the fetched records
if records:
    for record in records:
        print(f"City: {record.city}, Temperature: {record.temperature}°C, "
              f"Feels Like: {record.feels_like}°C, Weather: {record.main}, "
              f"Timestamp: {record.timestamp}")
else:
    print("No records found.")

# Close the session
session.close()
