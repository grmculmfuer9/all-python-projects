import requests

from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_FLIGHT_SEARCH_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
TEQUILA_API_KEY = "EXYqqz-8Z0zhfGjGoaQU7uvaNEFtxC57"


class FlightSearch:
    def __init__(self, max_stopovers=2):
        """Get IATA codes of cities or find flight details"""
        self.location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        self.header = {"content-type": "application/json", "apikey": TEQUILA_API_KEY}
        self.flight_price = None
        self.flight_price_data = None
        self.max_stopovers = max_stopovers
        self.header = {"content-type": "application/json", "apikey": TEQUILA_API_KEY}

    def get_iata_code(self, city_name):
        """Get IATA codes of the cities from tequila"""
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=self.location_endpoint, headers=self.header, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        flight_json_update_data = {
            "price": {
                "iataCode": code
            }
        }
        return flight_json_update_data

    def find_flight_details(self, start_city, destination_city, start_date, end_date, start_city_name,
                            destination_city_name):
        """Find details regarding the flight you want to have if present"""
        tequila_endpoint_params = {
            "fly_from": start_city,
            "fly_to": destination_city,
            "date_from": start_date,
            "date_to": end_date,
            "max_stopovers": self.max_stopovers,
            "curr": "USD"
        }
        self.flight_price_data = requests.get(url=TEQUILA_FLIGHT_SEARCH_ENDPOINT, headers=self.header,
                                              params=tequila_endpoint_params).json()
        try:
            self.flight_price = self.flight_price_data["data"][0]["price"]
        except KeyError:
            print("Flight booked too far in the future")
            return None
        except IndexError:
            if self.max_stopovers > 2:
                return "No flight for mentioned time"
            else:
                self.max_stopovers += 1
                self.find_flight_details(start_city=start_city, destination_city=destination_city,
                                         start_date=start_date, end_date=end_date,
                                         start_city_name=start_city_name, destination_city_name=destination_city_name)
            return None
        else:
            data = self.flight_price_data["data"][0]
            via_city = ""
            x = 0
            for x in range(len(data["route"])):
                if data["route"][x]["cityCodeTo"] == destination_city:
                    break
                via_city += data["route"][x]["cityTo"] + ", "
            via_city = via_city.strip(", ")
            flight_data = FlightData(start_city=start_city,
                                     destination_city=destination_city,
                                     start_date=start_date,
                                     end_date=end_date,
                                     via_city=via_city,
                                     start_airport=data["route"][0]["flyFrom"],
                                     destination_airport=data["route"][x]["flyTo"],
                                     max_stopovers=self.max_stopovers,
                                     price=data["price"],
                                     destination_city_name=destination_city_name)
        return flight_data
