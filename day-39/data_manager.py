import requests
from config import Config


class SheetyAPIError(Exception):
    pass


class DataManager:
    def __init__(self, config: Config):
        self._sheety_api_id_endpoint = config.sheety_api_id_endpoint
        self._sheety_bearer_token = config.sheety_bearer_token
        self._sheety_headers = {"Authorization": f"Bearer {self._sheety_bearer_token}"}
        self._sheety_url = (
            f"https://api.sheety.co/{self._sheety_api_id_endpoint}/flightDeals/prices"
        )

    def get_rows(self) -> dict:
        sheety_response = requests.get(self._sheety_url, headers=self._sheety_headers)

        if sheety_response.status_code != 200:
            raise SheetyAPIError

        return sheety_response.json()["prices"]

    def edit_row(self, row_id: int, iata_code: str) -> bool:
        parameters = {"price": {"iataCode": iata_code}}
        sheety_response = requests.put(
            self._sheety_url + f"/{row_id}",
            json=parameters,
            headers=self._sheety_headers,
        )

        if sheety_response.status_code != 200:
            print(
                f"Row {row_id} not edited. Error status{ sheety_response.status_code} error:{sheety_response.text}"
            )
            return False

        return True
