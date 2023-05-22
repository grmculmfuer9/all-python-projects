import datetime as dt
import random
import smtplib

import pandas


# 1. Update the birthdays.csv
def choose_a_random_letter():
    random_number = random.randint(1, 3)
    with open(f"letter_templates/letter_{random_number}.txt") as file:
        contents_of_birthday_letter = [i.strip() for i in file.readlines()]

    result_of_the_birthday_letter = ""
    for i in contents_of_birthday_letter:
        if i == "":
            result_of_the_birthday_letter += "\n"
        else:
            result_of_the_birthday_letter += i

    return result_of_the_birthday_letter


df = pandas.read_csv("birthdays.csv")

MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"

birthday_time_check = dt.datetime.now()
for (index, rows) in df.iterrows():
    if birthday_time_check.month == rows['month'] and birthday_time_check.day == rows['day']:
        result = choose_a_random_letter()
        result = result.replace("[NAME]", rows["name"])

        with smtplib.SMTP(host="smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=rows['email'],
                                msg=f"Subject:Happy Birthday!\n\n{result}")
