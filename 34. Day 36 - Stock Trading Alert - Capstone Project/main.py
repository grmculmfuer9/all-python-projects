import requests
import html
from twilio.rest import Client
import math
import re

STOCK = "TSLA"
COMPANY_NAME = "Tesla%Inc"
STOCK_MARKET_API_KEY = "7YU5HJQXF75U7DLB"
NEWS_API_KEY = "ca5f1ede9b13460cba88a42e5011f6de"
account_sid = "ACc34e902c45896dfcced95f82a98f1994"
auth_token = "3c52096efbbda521e0dea8c5e81897cd"

params_news_endpoint = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

params_stock_endpoint = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "apikey": STOCK_MARKET_API_KEY
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
negative = False

regex = re.compile(r'<[^>]+>')


def remove_html(string):
    return regex.sub('', string)


stock_data = requests.get(url=STOCK_ENDPOINT, params=params_stock_endpoint).json()["Time Series (Daily)"]
i = 0
data_of_two_previous_days = []
for (key, value) in stock_data.items():
    data_of_two_previous_days.append(float(value["4. close"]))
    i += 1
    if i >= 2:
        break

difference_between_two_prices = data_of_two_previous_days[1] - data_of_two_previous_days[0]
five_percent_of_actual_price = data_of_two_previous_days[1] * 0.05

if difference_between_two_prices < 0:
    negative = True
    difference_between_two_prices *= -1

if difference_between_two_prices <= five_percent_of_actual_price:
    news_data = requests.get(url=NEWS_ENDPOINT, params=params_news_endpoint).json()["articles"]
    # print(news_data)
    # breakpoint()
    news_data = news_data[:3]

    article_data = ""
    decrease = (difference_between_two_prices / data_of_two_previous_days[1]) * 100
    decrease = math.ceil(decrease)

    for i in news_data:
        if negative:
            symbol = "🟢"
        else:
            symbol = "🔴"
        article_data += f"\nTSLA: {symbol}{decrease}%\n"
        article_data += f"Headline: {html.unescape(i['title'])}\n"
        article_data += f"Brief: {html.unescape(i['description'])}\n\n"
    article_data = remove_html(article_data)

    print('sent')

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=article_data,
        from_="+12762779103",
        to="+923218050206"
    )
