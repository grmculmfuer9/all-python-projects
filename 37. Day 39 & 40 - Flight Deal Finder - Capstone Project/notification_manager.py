import os
import smtplib

import requests

from flight_data import FlightData

# ACCOUNT_SID_TWILIO = "AC5826dd334749f88cf27fe95b9e9381f3"
# AUTH_TOKEN_TWILIO = "763a00873fa0d62d6c1e96981705170e"
MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"
USERS_SHEETY_DATA_ENDPOINT = "https://api.sheety.co/fb2588459cd8ff692494ef2c3f9141b5/flightDeals/users"
USERS_SHEETY_DATA_ENDPOINT_USERNAME = os.environ.get("sheety_username")
USERS_SHEETY_DATA_ENDPOINT_PASSWORD = os.environ.get("sheety_password")
USERS_SHEETY_DATA_ENDPOINT_HEADER = {
    "Authorization": os.environ.get("sheety_endpoint_authorization")
}
START_CITY = "KHI"


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self, flight_data: FlightData, start_date, end_date):
        """Notify the user if flight price is within budget"""
        link = f"https://www.google.co.uk/flights?hl=en#flt={flight_data.start_city}." \
               f"{flight_data.destination_airport}." \
               f"{start_date}*{flight_data.destination_airport}.{flight_data.start_city}." \
               f"{end_date}"
        self.user_message = f"\nLow Price Alert! Only ${flight_data.price} to fly from Karachi-{START_CITY} " \
                            f"to {flight_data.destination_city_name}" \
                            f"-{flight_data.destination_city}, from {flight_data.start_date} to {flight_data.end_date}." \
                            f"\n" \
                            f"Passing through {flight_data.via_city} with {flight_data.max_stopovers} stopovers" \
                            f"\n\n" \
                            f"Take a look at this link:\n" \
                            f"{link}"

    def notify_the_user(self):
        """Send email to the use who are part of the club"""
        get_user_data_endpoint = requests.get(url=USERS_SHEETY_DATA_ENDPOINT,
                                              auth=(
                                                  USERS_SHEETY_DATA_ENDPOINT_USERNAME,
                                                  USERS_SHEETY_DATA_ENDPOINT_PASSWORD),
                                              headers=USERS_SHEETY_DATA_ENDPOINT_HEADER).json()["users"]
        for x in get_user_data_endpoint:
            user_email = x["email"]
            with smtplib.SMTP(host="smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(from_addr=MY_EMAIL,
                                    to_addrs=user_email,
                                    msg=f"Subject:Low Price Alert!\n\n{self.user_message}")
