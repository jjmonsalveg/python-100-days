import os
from datetime import datetime, timedelta

import requests
from dotenv import load_dotenv

load_dotenv()
_TOKEN = os.getenv("TOKEN")
_USERNAME = os.getenv("USERNAME")

domain_url = "https://pixe.la/v1/users"
graph_id = "graph1"
today = datetime.now()
yesterday = today - timedelta(days=1)
delete_pixel_url = (
    f"{domain_url}/{_USERNAME}/graphs/{graph_id}/{yesterday.strftime("%Y%m%d")}"
)
headers = {"X-USER-TOKEN": _TOKEN}

response = requests.delete(url=delete_pixel_url, headers=headers)

print(response.text)
print(response.status_code)
