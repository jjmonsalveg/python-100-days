import os

import requests
from dotenv import load_dotenv

load_dotenv()
_TOKEN = os.getenv("TOKEN")
_USERNAME = os.getenv("USERNAME")

domain_url = "https://pixe.la/v1/users"
create_graph_endpoint = f"/{_USERNAME}/graphs"

user_params = {
    "token": _TOKEN,
    "username": _USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# CREATE ACCOUNT
response = requests.post(url=domain_url, json=user_params)
print(response.text)
