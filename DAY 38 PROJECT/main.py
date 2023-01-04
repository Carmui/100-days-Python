import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 182
AGE = 25

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]

today_date = datetime.now().strftime("%m/%d/%Y")
today_hour = datetime.now().strftime("%H:%M:%S")

### ADDING EXERCISES
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, headers=headers, json=parameters)
result = response.json()

### ADDING DATA TO GOOGLE SHEET

for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": today_date,
            "time": today_hour,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheety_parameters, auth=('carmui', 'eglekekle123'))

    print(sheet_response.text)