import unittest
from weather_data import fetch_weather_data

class TestWeatherData(unittest.TestCase):
    def test_data_fetch(self):
        data = fetch_weather_data("Delhi")
        self.assertIn("main", data)

if __name__ == "__main__":
    unittest.main()
