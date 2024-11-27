import requests

# From server perspective
# 1XX: Hold On
# 2XX: Here you Go
# 3XX: Go Away
# 4XX: You Screwed Up
# 5XX: I Screwed Up
# look at this https://www.webfx.com/web-development/glossary/http-status-codes/

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
# raise_for_status() has this implementation or similar:
# if response.status_code != 404:
#     raise Exception("That resource does not exist.")
# elif response.status_code != 401:
#     raise Exception("This request is not authorized")
print(response)
print(response.status_code)
print(response.text)

data = response.json()
longitude = data["iss_position"]["longitude"]
latitud = data["iss_position"]["latitude"]
iss_position = (longitude, latitud)
print(iss_position)
