import os
import time
from datetime import datetime, timedelta

from config import Config
from data_manager import DataManager
from dotenv import load_dotenv
from flight_data import find_cheapest_flight
from flight_search import FlightSearch
from notification_manager import NotificationEmailManager, NotificationSMSManager

load_dotenv()


def get_iata_code(city: dict) -> str:
    current_iata_code = None

    if city and not city["iataCode"]:
        current_iata_code = flight_search.get_iata_city_code(city["city"])
        print(
            f"Update {city["id"]}, {city["city"]} with iata code { current_iata_code}"
        )
        data_manager.edit_price(city["id"], current_iata_code)

    current_iata_code = current_iata_code or (city and city["iataCode"])

    return current_iata_code


def get_cheapest_flight(current_iata_code: str, data_prices_response: dict, city: dict):
    cheapest_flight = find_cheapest_flight(data_prices_response)
    print(f"{current_iata_code}: ${cheapest_flight.price}")

    if float(city["lowestPrice"]) > cheapest_flight.price:
        print(f"New cheapest fligh for to {current_iata_code}")
        # notification_sms_manager.send(cheapest_flight)
        user_emails = data_manager.get_customer_emails()

        for email in user_emails:
            notification_email_manager.send(cheapest_flight, email)


amadeus_api_key = os.getenv("AMADEUS_API_KEY")
amadeus_api_secret = os.getenv("AMADEUS_API_SECRET")
sheety_api_id_endpoint = os.getenv("SHEETY_API_ID_ENPOINT")
sheety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")
twilio_account_sid = os.getenv("TWILIO_ACCOUNT_SID")
twilio_auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_from_number = os.getenv("TWILIO_FROM_NUMBER")
twilio_to_number = os.getenv("TWILIO_TO_NUMBER")
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD_SENDER")

source_city_iata_code = "MEX"

config = Config(
    sheety_api_id_endpoint=sheety_api_id_endpoint,
    sheety_bearer_token=sheety_bearer_token,
    amadeus_api_key=amadeus_api_key,
    amadeus_api_secret=amadeus_api_secret,
    email_from=sender_email,
    email_password=password,
    twilio_account_sid=twilio_account_sid,
    twilio_auth_token=twilio_auth_token,
    twilio_from_number=twilio_from_number,
    twilio_to_number=twilio_to_number,
)

data_manager = DataManager(config)
flight_search = FlightSearch(config)
notification_sms_manager = NotificationSMSManager(config)
notification_email_manager = NotificationEmailManager(config)

cities = data_manager.get_prices()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for city in cities:
    current_iata_code = get_iata_code(city)
    if current_iata_code:
        data_prices_response = flight_search.get_prices(
            source_city_iata_code,
            current_iata_code,
            tomorrow,
            six_month_from_today,
            is_direct=True,
        )

        if not (data_prices_response and data_prices_response["data"]):
            print(
                f"No direct flight to {current_iata_code}. Looking for indirect flights..."
            )
            data_prices_response = flight_search.get_prices(
                source_city_iata_code,
                current_iata_code,
                tomorrow,
                six_month_from_today,
                is_direct=False,
            )

        if not (data_prices_response and data_prices_response["data"]):
            print("No flight data")
            print(f"{current_iata_code}: N/A")
        else:
            get_cheapest_flight(current_iata_code, data_prices_response, city)

        time.sleep(2)
