from dataclasses import dataclass

from twilio.rest import Client

from config import Config
from flight_data import FlightData


@dataclass
class SMSMessage:
    from_number: str
    to_number: str
    body: str
    sid: str
    status: str


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self, config: Config):
        self._twilio_from_number = config.twilio_from_number
        self._twilio_to_number = config.twilio_to_number
        self._client = Client(config.twilio_account_sid, config.twilio_auth_token)

    def send(self, flight_data: FlightData) -> SMSMessage | None:
        body_text = (
            f"Low price alert! Only ${flight_data.price}, to fly"
            + f" from {flight_data.origin_airport} to {flight_data.destination_airport},"
            + f" on {flight_data.out_date} until {flight_data.return_date}"
        )

        message = self._client.messages.create(
            to=self._twilio_to_number,
            from_=self._twilio_from_number,
            body=body_text,
        )

        if message.status == "failed":
            return None

        print(f"sms sent:{body_text}")
        print(message.sid)
        print(message.status)

        return SMSMessage(
            from_number=self._twilio_from_number,
            to_number=self._twilio_to_number,
            body=body_text,
            sid=message.sid,
            status=message.status,
        )
