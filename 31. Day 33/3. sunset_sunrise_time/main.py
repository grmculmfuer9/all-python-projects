import datetime
import smtplib
import requests
import time

MY_LAT = 24.860735
MY_LONG = 67.001137
MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


def is_iss_overhead():
    lat_lng_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    lat_lng_response.raise_for_status()

    data_lat_lng = lat_lng_response.json()

    longitude = float(data_lat_lng["iss_position"]["longitude"])
    latitude = float(data_lat_lng["iss_position"]["latitude"])

    return MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LONG - 5 <= longitude <= MY_LONG + 5


def is_night():
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]

    hour_sunrise = int(sunrise.split("T")[1].split(":")[0])
    hour_sunset = int(sunset.split("T")[1].split(":")[0])
    hour_curr = datetime.datetime.now().hour

    return hour_curr >= hour_sunset or hour_curr <= hour_sunrise


while True:
    if is_iss_overhead() and is_night():
        time.sleep(3600)
        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="ninjacombo99@gmail.com",
                                msg="Subject:View the ISS 👆!\n\nView the ISS before the Sunrise")
    else:
        break
