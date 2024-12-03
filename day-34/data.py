import requests

parameters = {"amount": 18, "type": "boolean"}
response_api = requests.get("https://opentdb.com/api.php", params=parameters)
question_data = response_api.json()["results"]
