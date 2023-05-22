from smtplib import SMTP

import lxml
import requests
from bs4 import BeautifulSoup

AMAZON_URL = "https://www.amazon.com/Hathaway-Foosball-56-Table-Cover/dp/B01LBBDUF8/ref=sr_1_35?crid=2GDFHNQTN22HQ" \
             "&keywords=foosball&qid=1678870075&sprefix=foosbal%2Caps%2C507&sr=8-35"
BUDGET_PRICE = 80
MY_EMAIL = "hellomy98d@gmail.com"
PASSWORD = "aeyzoterumrnhoux"

amazon_header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 "
                  "Safari/537.36 OPR/96.0.0.0"
}

response = requests.get(url=AMAZON_URL, headers=amazon_header)

amazon_html_code = BeautifulSoup(markup=response.text, parser=lxml, features="lxml")
price_before_decimal = amazon_html_code.find(name="span", class_="a-price-whole").text
price_after_decimal = amazon_html_code.find(name="span", class_="a-price-fraction").text
final_price = float(f"{price_before_decimal}{price_after_decimal}")

title = amazon_html_code.find(id="productTitle").text.strip()
if final_price <= BUDGET_PRICE:
    message = f"{title} is not at {final_price}\nGo to this link to purchase the product {AMAZON_URL}"

    with SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs="ninjacombo99@gmail.com",
                            msg="Subject:Amazon Foosball Table Price Alert!\n\n"
                                f"{message}")
