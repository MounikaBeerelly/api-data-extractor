"""
main.py

Entry point for the API Data Extractor project.
"""
from weather_api import WeatherAPI

def main():
    """
    Main entry point for the calculator application.
    """
    weatherdata = WeatherAPI(
        access_key="94e876191d384feb0e64597adf2635f6",
        base_url="http://api.weatherstack.com/current",
        location="New York"
    )

    data = weatherdata.get_current_weather()
    print(data)

if __name__ == "__main__":
    main()
