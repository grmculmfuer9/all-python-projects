class FlightData:
    def __init__(self, start_city, destination_city, via_city, start_airport, destination_airport,
                 max_stopovers, start_date, end_date, price, destination_city_name):
        """Store all the details of the flight"""
        self.start_city = start_city
        self.destination_city = destination_city
        self.via_city = via_city
        self.start_airport = start_airport
        self.destination_airport = destination_airport
        self.destination_city_name = destination_city_name
        self.price = price
        self.max_stopovers = max_stopovers
        self.start_date = start_date
        self.end_date = end_date
