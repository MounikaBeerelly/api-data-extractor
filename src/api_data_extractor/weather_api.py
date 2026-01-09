"""
weather_api.py

responsible for handling API requests.
"""
import requests

class WeatherAPI:
    """Fetching Weather data from a third-party API."""

    def __init__(self, access_key: str, base_url: str, location: str, default_timeout: int = 10):
        self.access_key = access_key
        self.base_url = base_url
        self.location = location
        self.default_timeout = default_timeout

    def get_current_weather(self):
        """
        Fetch current weather information for a given location.
        """
        params = {
            "query": self.location,
            "access_key": self.access_key
        }
        try:
            response = requests.get(
                self.base_url,
                params=params,
                timeout=self.default_timeout
                )

            response.raise_for_status()
            return {
                "message": "Successfully fetched weather data.",
                "data": response.json()
            }
        except requests.exceptions.RequestException as err:
            raise RuntimeError(f"Failed to fetch weather data: {err}") from err
