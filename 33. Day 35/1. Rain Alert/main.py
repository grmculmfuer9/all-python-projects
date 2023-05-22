import requests
import os
from twilio.rest import Client

# from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient()
# proxy_client.session.proxies = {'https': os.environ['https_proxy']}
OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = "08341857fd4d92a3cca11b5cff0bad47"
api_key = os.environ.get("OWM_API_KEY")
account_sid = "ACc34e902c45896dfcced95f82a98f1994"
auth_token = "3c52096efbbda521e0dea8c5e81897cd"
will_rain = False

weather_params = {
    "lat": 24.860735,
    "lon": 67.001137,
    "exclude": "current,minutely,daily",
    "appid": api_key
}

response = requests.get(OWN_ENDPOINT, params=weather_params)
data = response.json()
# weather_slice = data["hourly"][:12]
# for hour_data in weather_slice:
#     condition_code = int(hour_data["weather"][0]["id"])
#     if not will_rain and condition_code < 700:
#         will_rain = True

if will_rain:
    print("Bring an Umbrella")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="Shut Up",
        from_="+13159034687",
        to="+923218050206"
    )

client = Client(account_sid, auth_token)
message = client.messages.create(
    body="Take umbrella or shut up",
    from_="+13159034687",
    to="+923323224701"
)
