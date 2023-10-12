import requests
from datetime import datetime, timedelta

import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("KEY")

class FlightSearch:
    def __init__(self, city):
        self.location_endpoint = "https://api.tequila.kiwi.com/locations/query"
        self.flight_key = key
        self.headers = {
            "apikey": self.flight_key
        }
        parameters = {
            "term": city,
            "location_types": "city",
        }
        self.location_data = requests.get(url=self.location_endpoint, params=parameters, headers=self.headers).json()
