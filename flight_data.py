import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()
key = os.environ.get("KEY")

class FlightData:
    def __init__(self, destination):
        self.departure_city_code = "DEL"
        self.stop_overs = 0
        self.via_city = ""
        self.destination_city_code = destination
        self.departure_city = "New Delhi"
        self.search_endpoint = "https://api.tequila.kiwi.com/v2/search"
        self.flight_key = key
        self.headers = {
            "apikey": self.flight_key
        }
        tomorrow = (datetime.now() + timedelta(1)).strftime("%d/%m/%Y")
        date_after_six_months = (datetime.now() + timedelta(180)).strftime("%d/%m/%Y")
        return_range_start = (datetime.now() + timedelta(8)).strftime("%d/%m/%Y")
        return_range_end = (datetime.now() + timedelta(29)).strftime("%d/%m/%Y")

        flight_parameters = {
            "fly_from": "DEL",
            "fly_to": destination,
            "date_from": tomorrow,
            "date_to": date_after_six_months,
            "curr": "INR",
            "max_stopovers": 0,
            "return_from": return_range_start,
            "return_to": return_range_end,
            "vehicle_type": "aircraft",
        }

        try:
            self.flight_data = requests.get(url=self.search_endpoint, params=flight_parameters, headers=self.headers).json()["data"][0]
        except:
            self.stop_overs = 2
            new_flight_parameters = {
                "fly_from": "DEL",
                "fly_to": destination,
                "date_from": tomorrow,
                "date_to": date_after_six_months,
                "curr": "INR",
                "max_stopovers": 2,
                "return_from": return_range_start,
                "return_to": return_range_end,
                "vehicle_type": "aircraft",
            }
            self.flight_data = requests.get(url=self.search_endpoint, params=new_flight_parameters, headers=self.headers).json()["data"][0]
            self.via_city = self.flight_data["route"][0]["cityTo"]
            self.return_date = self.flight_data["route"][2]["local_departure"].split("T")[0]
        else:
            self.return_date = self.flight_data["route"][1]["local_departure"].split("T")[0]
        finally:
            self.price = self.flight_data["price"]
            self.departure_airport_code = self.flight_data["flyFrom"]
            self.arrival_airport_code = self.flight_data["flyTo"]
            self.flight_date = self.flight_data["route"][0]["local_departure"].split("T")[0]