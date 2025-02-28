import smtplib
from dataclasses import dataclass

from config import Config
from flight_data import FlightData
from twilio.rest import Client


@dataclass
class SMSMessage:
    from_number: str
    to_number: str
    body: str
    sid: str
    status: str


@dataclass
class EmailMessage:
    from_email: str
    to_email: str
    subject: str
    body: str


class NotificationEmailManager:
    def __init__(self, config: Config):
        self._email_from = config.email_from
        self._email_password = config.email_password

    def send(self, flight_data: FlightData, to_email: str) -> EmailMessage | None:
        if flight_data.stops == 0:
            body_text = (
                f"Low price alert! Only GBP {flight_data.price} to fly direct "
                f"from {flight_data.origin_airport} to {flight_data.destination_airport}, "
                f"on {flight_data.out_date} until {flight_data.return_date}."
            )
        else:
            body_text = (
                f"Low price alert! Only GBP {flight_data.price} to fly "
                f"from {flight_data.origin_airport} to {flight_data.destination_airport}, "
                f"with {flight_data.stops} stop(s) "
                f"departing on {flight_data.out_date} and returning on {flight_data.return_date}."
            )

        message = EmailMessage(
            from_email=self._email_from,
            to_email=to_email,
            subject="Low price alert!",
            body=body_text,
        )

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self._email_from, password=self._email_password)
            connection.sendmail(
                from_addr=message.from_email,
                to_addrs=message.to_email,
                msg="Subject:" + message.subject + "\n\n" + message.body,
            )

        print(f"email sent:{body_text}")

        return message


class NotificationSMSManager:
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
