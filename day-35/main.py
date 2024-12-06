import os

import requests
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

API_KEY = os.getenv("OVM_API_KEY")
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
from_phone_number = os.getenv("TWILIO_FROM_NUMBER")
to_phone_number = os.getenv("TWILIO_TO_NUMBER")

MY_LAT = 6.244203
MY_LONG = -75.581215
url = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {"lat": MY_LAT, "lon": MY_LONG, "appid": API_KEY, "cnt": 4}

response = requests.get(url, params=parameters)
response.raise_for_status()

weather = response.json()["list"]
will_rain = False

for forecast in weather:
    code = int(forecast["weather"][0]["id"])
    if code < 700:
        will_rain = True
        break

if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=to_phone_number,
        from_=from_phone_number,
        body="It's going to rain today. Remember to bring an ☔️",
    )

    print(message.sid)
    print(message.status)

# print(list(map(lambda forecast: forecast["weather"][0]["id"] , weather)))
# print(any(map(lambda forecast: forecast["weather"][0]["id"] < 700 , weather)))
# if (any(map(lambda forecast: forecast["weather"][0]["id"] < 700 , weather))):
#     print("Bring an umbrella")
