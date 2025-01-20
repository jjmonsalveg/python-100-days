from dataclasses import dataclass


@dataclass(frozen=True)
class Config:
    sheety_api_id_endpoint: str
    sheety_bearer_token: str
    amadeus_api_key: str
    amadeus_api_secret: str
    twilio_account_sid: str
    twilio_auth_token: str
    twilio_from_number: str
    twilio_to_number: str
