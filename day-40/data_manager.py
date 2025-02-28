import requests
from config import Config


class SheetyAPIError(Exception):
    pass


class DataManager:
    def __init__(self, config: Config):
        self._sheety_api_id_endpoint = config.sheety_api_id_endpoint
        self._sheety_bearer_token = config.sheety_bearer_token
        self._sheety_headers = {"Authorization": f"Bearer {self._sheety_bearer_token}"}
        self._sheety_prices_url = (
            f"https://api.sheety.co/{self._sheety_api_id_endpoint}/flightDeals/prices"
        )
        self._sheety_users_url = (
            f"https://api.sheety.co/{self._sheety_api_id_endpoint}/flightDeals/users"
        )

    def get_prices(self) -> dict:
        sheety_response = requests.get(
            self._sheety_prices_url, headers=self._sheety_headers
        )

        if sheety_response.status_code != 200:
            raise SheetyAPIError

        return sheety_response.json()["prices"]

    def edit_price(self, row_id: int, iata_code: str) -> bool:
        parameters = {"price": {"iataCode": iata_code}}
        sheety_response = requests.put(
            self._sheety_prices_url + f"/{row_id}",
            json=parameters,
            headers=self._sheety_headers,
        )

        if sheety_response.status_code != 200:
            print(
                f"Row {row_id} not edited. Error status{ sheety_response.status_code} error:{sheety_response.text}"
            )
            return False

        return True

    def get_customer_emails(self) -> list[str]:
        sheety_response = requests.get(
            self._sheety_users_url, headers=self._sheety_headers
        )

        if sheety_response.status_code != 200:
            raise SheetyAPIError

        emails = [user["whatIsYourEmail?"] for user in sheety_response.json()["users"]]
        return emails
