import smtplib

MY_EMAIL = "hellomy98d@gmail.com"
MY_PASSWORD = "aeyzoterumrnhoux"

with smtplib.SMTP(host="smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.sendmail(from_addr=MY_EMAIL,
                        to_addrs="ninjacombo99@gmail.com",
                        msg="Subject:Hello!\n\nThis is the body of my email")
