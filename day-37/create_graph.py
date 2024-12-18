import os

import requests
from dotenv import load_dotenv

load_dotenv()
_TOKEN = os.getenv("TOKEN")
_USERNAME = os.getenv("USERNAME")

domain_url = "https://pixe.la/v1/users"
create_graph_endpoint = f"/{_USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cyclin Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}
headers = {"X-USER-TOKEN": _TOKEN}
create_graph_response = requests.post(
    url=domain_url + create_graph_endpoint, json=graph_config, headers=headers
)
print(create_graph_response.text)
# to see it go to https://pixe.la/v1/users/python-100/graphs/graph1.html
