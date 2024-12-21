import os
from datetime import datetime

import requests
from dotenv import load_dotenv

load_dotenv()

nutrionix_api_key = os.getenv("NUTRIONIX_API_KEY")
nutrionix_api_app_id = os.getenv("NUTRIONIX_API_APP")
sheeety_api_id_endpoint = os.getenv("SHEETY_API_ID_ENPOINT")
sheeety_bearer_token = os.getenv("SHEETY_BEARER_TOKEN")

sheety_post_url = (
    f"https://api.sheety.co/{sheeety_api_id_endpoint}/workoutTracking/workouts"
)

domain_nutrionix = "https://trackapi.nutritionix.com"
headers = {
    "x-app-id": nutrionix_api_app_id,
    "x-app-key": nutrionix_api_key,
    "Content-Type": "application/json",
}

input_prompt = input("Tell me wich exercises you did: ")
nutrionix_body = {
    "query": input_prompt,
    "gender": "male",
    "weight_kg": 80,
    "height_cm": 178,
    "age": 32,
}
nutrionix_response = requests.post(
    domain_nutrionix + "/v2/natural/exercise", headers=headers, json=nutrionix_body
)
print(nutrionix_response.text)
print(nutrionix_response.status_code)

exercises = nutrionix_response.json()["exercises"]
today = datetime.now()

sheety_headers = {"Authorization": f"Bearer {sheeety_bearer_token}"}

for exercise in exercises:
    calories = exercise["nf_calories"]
    duration = exercise["duration_min"]
    exercise_name = exercise["name"].title()
    sheety_body = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": exercise_name,
            "duration": duration,
            "calories": calories,
        }
    }
    sheety_response = requests.post(
        sheety_post_url, json=sheety_body, headers=sheety_headers
    )
    print(sheety_response.text)
    print(sheety_response.status_code)

# tutor solution: https://gist.github.com/angelabauer/2e147663f998bbcf7b403c6c83f56a14
