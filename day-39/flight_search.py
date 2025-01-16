import requests
from datetime import datetime


class GetTokenApiError(Exception):
    pass


class GetIATACodesError(Exception):
    pass


class FlightSearch:
    """
    Class is responsible for talking to the Flight Search API.
    """

    def __init__(self, config: dict):
        self._amadeus_api_key = config["amadeus_api_key"]
        self._amadeus_api_secret = config["amadeus_api_secret"]
        self._amadeus_domain = "https://test.api.amadeus.com/v1"
        self._amadeus_domain_v2 = "https://test.api.amadeus.com/v2"
        self._amadeus_token = None

    def get_prices(
        self,
        src_iata_code: str,
        tgt_iata_code: str,
        from_time: datetime,
        to_time: datetime,
    ) -> dict:
        path = "/shopping/flight-offers"
        amadeus_headers = {"Authorization": self._get_authorization_header()}
        query = {
            "originLocationCode": src_iata_code,
            "destinationLocationCode": tgt_iata_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 1,
            "nonStop": "true",
            "currencyCode": "USD",
            "max": "10",
        }
        amadeus_response = requests.get(
            self._amadeus_domain_v2 + path, params=query, headers=amadeus_headers
        )
        if amadeus_response.status_code != 200:
            print(f"check_flights() response code: {amadeus_response.status_code}")
            print(
                "There was a problem with the flight search.\n"
                "For details on status codes, check the API documentation:\n"
                "https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api"
                "-reference"
            )
            print("Response body:", amadeus_response.text)
            return None

        return amadeus_response.json()

    def get_iata_city_code(self, keyword_city: str) -> str:
        path = "/reference-data/locations/cities"
        amadeus_headers = {"Authorization": self._get_authorization_header()}
        amadeus_response = requests.get(
            self._amadeus_domain + path,
            params={"keyword": keyword_city},
            headers=amadeus_headers,
        )

        if amadeus_response.status_code != 200:
            raise GetIATACodesError

        try:
            iata_city_code = amadeus_response.json()["data"][0]["iataCode"]
        except IndexError:
            print(f"IndexError: No airport code found for {keyword_city}.")
            return "N/A"
        except KeyError:
            print(f"KeyError: No iata code found for {keyword_city}.")
            return "Not Found"
        return iata_city_code

    def _get_token(self):
        if self._amadeus_token:
            return self._amadeus_token

        path = "/security/oauth2/token"
        parameters = {
            "grant_type": "client_credentials",
            "client_id": self._amadeus_api_key,
            "client_secret": self._amadeus_api_secret,
        }
        amadeus_response = requests.post(
            self._amadeus_domain + path,
            headers={"Content-Type": "application/x-www-form-urlencoded"},
            data=parameters,
        )

        if amadeus_response.status_code != 200:
            raise GetTokenApiError

        self._amadeus_token = amadeus_response.json()["access_token"]

        return self._amadeus_token

    def _get_authorization_header(self):
        return f"Bearer {self._get_token()}"
