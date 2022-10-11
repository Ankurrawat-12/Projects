import datetime as dt
import smtplib
from random import randint
import pandas

MY_EMAIL = "ankurrawatc6rcitt@gmail.com"
PASSWORD = "b(O3eTdsH8##g"

data = pandas.read_csv("birthdays.csv").to_dict(orient="records")
now = dt.datetime.now()
day = now.day
month = now.month
for n in range(len(data)):
    if data[n]["day"] == day and data[n]["month"] == month:
        receivers_email = data[n]["email"]
        receivers_name = data[n]["name"]
        with open(f"letter_templates/letter_{randint(1,3)}.txt") as letter:
            letter_temp = letter.read()
            new_letter = letter_temp.replace("[NAME]", receivers_name)
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=receivers_email, msg=f"Subject:Happy Birthday\n\n"
                                                                                  f"{new_letter}")
