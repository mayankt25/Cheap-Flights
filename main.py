from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from datetime import datetime
from get_input import GetInput

get_input = GetInput()
data_manager = DataManager()

for data in data_manager.sheet_data:
    if data["iataCode"] == "":
        flight_search = FlightSearch(data["city"].title())
        city_data = flight_search.location_data
        if len(city_data["locations"]) != 0:
            city_code = city_data["locations"][0]["code"]
            data_manager.update_sheet_data(id=data["id"], code=city_code)

for data in data_manager.sheet_data:
    destination_code = data["iataCode"]
    destination_city = data["city"].title()
    lowest_price = data["lowestPrice"]
    flight_data = FlightData(destination_code)
    departure_city = flight_data.departure_city

    if flight_data.price < lowest_price:
        departure_airport_code = flight_data.departure_airport_code
        arrival_airport_code = flight_data.arrival_airport_code
        flight_date = datetime.strptime(flight_data.flight_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        return_date = datetime.strptime(flight_data.return_date, "%Y-%m-%d").strftime("%d/%m/%Y")
        message = f"Low price alert! Only Rs. {flight_data.price} to fly from {departure_city}-{departure_airport_code} to {destination_city}-{arrival_airport_code}, from {flight_date} to {return_date}.\n"

        if flight_data.stop_overs != 0:
            message += f"Flight has 1 stop over, via {flight_data.via_city}.\n"

        message += f"https://www.makemytrip.com/flight/search?itinerary={departure_airport_code}-{arrival_airport_code}-{flight_date}_{arrival_airport_code}-{departure_airport_code}-{return_date}&tripType=R&paxType=A-1_C-0_I-0&intl=true&cabinClass=E&ccde=IN&lang=eng"

        notification_manager = NotificationManager()
        notification_manager.send_emails(message)