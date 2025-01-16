import os
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

load_dotenv()

amadeus_api_key = os.getenv("AMADEUS_API_KEY")
amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
sheety_api_id_endpoint = os.getenv("SHEETY_API_ID_ENPOINT")
sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_from_number = os.getenv("TWILIO_FROM_NUMBER")
twilio_to_number = os.getenv("TWILIO_TO_NUMBER")

source_city_iata_code = "MEX"

# TODO: move to be a dataclass
config = {
    "sheety_api_id_endpoint": sheety_api_id_endpoint,
    "sheety_bearer_token": sheety_bearer_token,
    "amadeus_api_key": amadeus_api_key,
    "amadeus_api_secret": amadeus_api_secret,
    "twilio_account_sid": twilio_account_sid,
    "twilio_auth_token": twilio_auth_token,
    "twilio_from_number": twilio_from_number,
    "twilio_to_number": twilio_to_number,
}

data_manager = DataManager(config)
flight_search = FlightSearch(config)
notification_manager = NotificationManager(config)

cities = data_manager.get_rows()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for city in cities:
    current_iata_code = None

    if city and not city["iataCode"]:
        current_iata_code = flight_search.get_iata_city_code(city["city"])
        print(
            f"Update {city["id"]}, {city["city"]} with iata code { current_iata_code}"
        )
        data_manager.edit_row(city["id"], current_iata_code)

    current_iata_code = current_iata_code or (city and city["iataCode"])

    if current_iata_code:
        data_prices_response = flight_search.get_prices(
            source_city_iata_code, current_iata_code, tomorrow, six_month_from_today
        )
        if data_prices_response and data_prices_response["data"]:
            cheapest_flight = find_cheapest_flight(data_prices_response)
            print(f"{current_iata_code}: ${cheapest_flight.price}")

            if float(city["lowestPrice"]) > cheapest_flight.price:
                print(f"New cheapest fligh for to {current_iata_code}")
                notification_manager.send(cheapest_flight)

            # Slowing down requests to avoid rate limit
            time.sleep(2)
        else:
            print("No flight data")
            print(f"{current_iata_code}: N/A")
