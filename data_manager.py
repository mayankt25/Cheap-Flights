import requests
import os
from dotenv import load_dotenv

load_dotenv()
token = os.environ.get("TOKEN")
api = os.environ.get("LINK")

class DataManager:
    def __init__(self):
        self.sheety_api = api
        sheety_prices_api = f"{self.sheety_api}/prices"
        self.sheety_token = "Bearer " + token
        self.headers = {
            "Authorization": self.sheety_token,
        }
        self.sheet_data = requests.get(url=sheety_prices_api, headers=self.headers).json()["prices"]

    def update_sheet_data(self, id, code):
        update_api = f"{self.sheety_api}/prices/{id}"
        update_config = {
            "price": {
                "iataCode": code,
            }
        }
        self.update_response = requests.put(url=update_api, json=update_config, headers=self.headers)
        print(self.update_response.text)

    def update_user_data(self, f_name, l_name, email):
        sheety_user_api = f"{self.sheety_api}/users"
        user_data_config = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email,
            }
        }
        self.update_response = requests.post(url=sheety_user_api, json=user_data_config, headers=self.headers)

    def get_user_data(self):
        sheety_user_api = f"{self.sheety_api}/users"
        self.user_data = requests.get(url=sheety_user_api, headers=self.headers).json()["users"]
        return self.user_data