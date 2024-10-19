# Weather Monitoring Application

## Overview
The **Weather Monitoring Application** is a Python-based system that fetches, stores, and visualizes real-time weather data from multiple cities. The application can also send alerts if specific weather conditions are detected, making it useful for monitoring and tracking weather patterns.

## Features
- **Real-Time Data Fetching**: Collects up-to-date weather data from various locations.
- **Data Storage**: Stores data in a local SQLite database for easy retrieval and analysis.
- **Command-Line Interface**: Displays fetched data in a user-friendly format.
- **Visualization**: Provides visual representations of weather patterns.
- **Alert System**: Triggers alerts based on predefined weather conditions.

## Design Choices
- **Programming Language**: Python was chosen for its simplicity and rich ecosystem of libraries.
- **Database**: SQLite was used due to its lightweight nature, making it easy to store data locally.
- **Containerization**: Docker is employed to ensure consistent deployment across different environments.
- **Modular Design**: The project is broken down into separate modules, making it easy to maintain and extend.

## Prerequisites
- [Python 3.12.5](https://www.python.org/downloads/)
- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)

## Project Structure
weather-monitoring/
- │
- ├── src/
- │   ├── alert_system.py
- │   ├── config.py
- │   ├── database.py
- │   ├── main.py
- │   ├── view_data.py
- │   ├── visualization.py
- │   └── weather_data.py
- ├
- ├─ weather-monitoring_vscode.png
- ├── .dockerignore
- ├── docker-compose.yml
- ├── Dockerfile
- ├── requirements.txt
- ├── README.md
- └── weather_data.db


## 2. Running the Application Using Docker
Ensure Docker and Docker Compose are installed on your system. Follow the steps below to build and run the application using Docker:

## **Step 1: Build and Run Containers**
- Copy code
- docker-compose up --build
## **Step 2: Access the Application**
- The application will automatically start fetching weather data once the containers are up.
- The fetched data will be stored in the weather_data.db file, which is part of the Docker container.
## 3. Manual Setup (Without Docker)
-If you prefer to run the application manually:

## **Step 1: Set Up a Virtual Environment**
- Copy code
- python -m venv venv
   source venv/bin/activate   # On Windows, use: venv\Scripts\activate
## **Step 2: Install Python Dependencies**
- Copy code
- pip install -r requirements.txt
## **Step 3: Run the Application**
- Copy code
- python src/main.py
## Dependencies
- The following dependencies are required to run the application:

**Python Libraries:**
**requests**: For fetching weather data
**sqlalchemy**: For database management
**pandas**: For data manipulation and visualization
**matplotlib**: For generating visual plots
**Docker**: For containerizing the application
**SQLite**: For local database storage
-Dependencies are listed in the requirements.txt file and will be installed when you run the pip install command.

## Usage
-Once the application is running, it will:

- Fetch and store weather data periodically.
- Display weather data in the command line.
- Allow viewing of the stored weather data using:
- Copy code
- **python src/view_data.py**
- Visualize weather trends by executing:
- Copy code
- **python src/visualization.py**
- Send alerts for specific weather conditions as configured in src/alert_system.py.
## **Screenshots**
- Below is a screenshot of the application running:
![weather-monitoring_vscode](https://github.com/user-attachments/assets/2e8fe82b-a9f4-4617-a505-f85c829a4d59)
## **Design Considerations**
**Ease of Use**: The application is designed to be easy to set up and run, even for users who are not familiar with programming.
**Scalability**: Modular code structure allows easy extension of the application, e.g., adding more cities or integrating new alert conditions.
**Portability**: Docker ensures the application can run consistently across different environments without manual setup.
## **Testing**
- Unit tests are included to validate the main functionalities. To run tests:

- Copy code
- python -m unittest discover
## **Known Issues**
-The application currently fetches data for a limited number of cities. Future improvements will include the ability to add more cities dynamically.
Alerts are limited to basic weather conditions. Expanding alert types is planned.
## **Future Enhancements**
**Dynamic City Addition**: Add cities dynamically without modifying the code.
**Web Interface**: A simple web interface to display weather data and graphs.
**Enhanced Alerts**: More detailed and customizable alerts.
**Author**
Kanukuntla Anjana
