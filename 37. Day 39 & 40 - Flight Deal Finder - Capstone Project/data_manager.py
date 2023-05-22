import os
import requests

SHEETY_ENDPOINT = "https://api.sheety.co/fb2588459cd8ff692494ef2c3f9141b5/flightDeals/prices"
SHEETY_ENDPOINT_PUT = "https://api.sheety.co/fb2588459cd8ff692494ef2c3f9141b5/flightDeals/prices"
SHEETY_USERNAME = os.environ.get("sheety_username")
SHEETY_PASSWORD = os.environ.get("sheety_password")


class DataManager:
    def __init__(self):
        """Get or update data from Google sheets regarding cities, IATA codes, or prices"""
        self.sheety_response = None
        self.sheety_endpoint_header = {
            "Authorization": os.environ.get("sheety_endpoint_authorization")
        }

    def get_sheety_response(self):
        """Get all the cities stored with IATA codes and budget prices in Google Sheets"""
        self.sheety_response = requests.get(url=SHEETY_ENDPOINT, auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                                            headers=self.sheety_endpoint_header)
        self.sheety_response.raise_for_status()
        self.sheety_response = self.sheety_response.json()

    def update_sheety_data_iata_code(self, flight_json_update_data, x):
        """Update the IATA codes in case they are not present their"""
        final_sheety_url = f"{SHEETY_ENDPOINT_PUT}/{x['id']}"
        sheety_response_put = requests.put(url=f"{final_sheety_url}", auth=(SHEETY_USERNAME, SHEETY_PASSWORD),
                                           headers=self.sheety_endpoint_header, json=flight_json_update_data)
        sheety_response_put.raise_for_status()
