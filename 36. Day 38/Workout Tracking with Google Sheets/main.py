from datetime import datetime
import os
import requests

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
SHETTY_USERNAME = os.environ.get("sheety_username")
SHETTY_PASSWORD = os.environ.get("sheety_password")

sheety_endpoint_header = {
    "Authorization": os.environ.get("sheety_endpoint_authorization")
}

NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/34047492f0225988e777518e66546a4b/myWorkout/workouts"
CURRENT_DATE = datetime.now().strftime("%d/%m/%Y")
CURRENT_TIME = datetime.now().strftime("%H:%M:%S")
response_sheety = requests.get(url=SHEETY_ENDPOINT, headers=sheety_endpoint_header,
                               auth=(SHETTY_USERNAME, SHETTY_PASSWORD)).json()

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

nutritionix_json = {
    "query": input("What exercises have you completed until now?\n"),
    "gender": "male",
    "weight_kg": "62",
    "height_cm": "173.5",
    "age": "18"
}

sheety_endpoint_json = {'workouts': {}}

response_nutritionix = requests.post(url=NUTRITIONIX_ENDPOINT, headers=nutritionix_headers, json=nutritionix_json). \
    json()

response_sheet = {}
for exercise in response_nutritionix["exercises"]:
    sheety_endpoint_json = {
        "workout": {
            "date": CURRENT_DATE,
            "time": CURRENT_TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response_sheety = requests.post(url=SHEETY_ENDPOINT, auth=(SHETTY_USERNAME, SHETTY_PASSWORD),
                                    headers=sheety_endpoint_header,
                                    json=sheety_endpoint_json).json()
print(response_sheety)
