import requests
import os
from twilio.rest import Client

OMW_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
## HIDDEN KEYS
api_key = ""
account_sid = os.environ['TWILIO_ACCOUNT_SID']=""
auth_token = os.environ['TWILIO_AUTH_TOKEN']=""

weather_params = {
    "lat": 51.5085,
    "lon": -0.1257,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OMW_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:4]

will_rain = False

for hour_data in weather_slice:
    condition = int(hour_data["weather"][0]["id"])
    if condition < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring umbrella!",
        from_="+15625739829",
        to= "+48501095044"
        )

print(message.sid)

#print(weather_data["hourly"][0]["weather"][0])