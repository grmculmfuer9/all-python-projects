import os
from datetime import datetime, timedelta

import requests

from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

USERS_SHEETY_DATA_ENDPOINT = "https://api.sheety.co/fb2588459cd8ff692494ef2c3f9141b5/flightDeals/users"
USERS_SHEETY_DATA_ENDPOINT_USERNAME = os.environ.get("sheety_username")
USERS_SHEETY_DATA_ENDPOINT_PASSWORD = os.environ.get("sheety_password")
USERS_SHEETY_DATA_ENDPOINT_HEADER = {
    "Authorization": os.environ.get("sheety_endpoint_authorization")
}
START_CITY = "KHI"

data_manager = DataManager()
flight_search = FlightSearch()

data_manager.get_sheety_response()
sheety_response = data_manager.sheety_response

date = datetime.now() + timedelta(days=180)
start_date = datetime.now().strftime("%d/%m/%Y")
end_date = f"{date.day}/{date.month}/{date.year}"

start_date_for_email = datetime.now().strftime("%Y-%m-%d")
end_data_for_email = f"{date.year}-{str(date.month).zfill(2)}-{date.day}"

users = int(input("How many users want to be part of the club?\n"))
count_users = 0
while count_users < users:
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")

    email_incorrect = True
    email = ""
    while email_incorrect:
        email = input("What is your email address?\n")
        retyped_email = input("Confirm your email address:\n")
        if email == retyped_email:
            email_incorrect = False
        else:
            print("Your email addresses does not match. Please try again!")

    post_user_json_data = {
        "user": {
            "firstName": first_name,
            "lastName": last_name,
            "email": email
        }
    }
    post_user_data = requests.post(url=USERS_SHEETY_DATA_ENDPOINT,
                                   auth=(USERS_SHEETY_DATA_ENDPOINT_USERNAME, USERS_SHEETY_DATA_ENDPOINT_PASSWORD),
                                   headers=USERS_SHEETY_DATA_ENDPOINT_HEADER,
                                   json=post_user_json_data)
    count_users += 1
print(sheety_response)
for x in sheety_response["prices"]:
    flight_json_update_data = flight_search.get_iata_code(x["city"])

    if x["iataCode"] == "":
        data_manager.update_sheety_data_iata_code(flight_json_update_data=flight_json_update_data, x=x)

for x in sheety_response["prices"]:
    flight_data = flight_search.find_flight_details(start_city=START_CITY, destination_city=x["iataCode"],
                                                    start_date=start_date, end_date=end_date,
                                                    start_city_name="Karachi", destination_city_name=x["city"])
    if flight_data is None:
        continue
    if flight_data.price <= x["lowestPrice"]:
        notification_manager = NotificationManager(flight_data, start_date_for_email, end_data_for_email)
        notification_manager.notify_the_user()
