from datetime import datetime

import requests

MY_LAT = 6.244203
MY_LONG = -75.581215
parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
