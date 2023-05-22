import smtplib
import datetime as dt
import random

date_time = dt.datetime.now()
MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"
COUSIN2_EMAIL = "shahrs55555@gmail.com"
BROTHER2_EMAIL = "haseebadnan2257@gmail.com"
BROTHER3_EMAIL = "hunainadnan123@gmail.com"
MY_ANOTHER_EMAIL = "ninjacombo99@gmail.com"
PAPA_EMAIL = "adnansaleem007@hotmail.com"

if date_time.weekday() == 2:
    with open(file="quotes.txt") as file:
        quotes = [i.strip() for i in file.readlines()]

    random_quote = random.choice(quotes)

    with smtplib.SMTP(host="smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)

        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=f"{PAPA_EMAIL}",
                            msg="Subject:Motivational Quote!\n\n"
                                f"{random_quote}")
