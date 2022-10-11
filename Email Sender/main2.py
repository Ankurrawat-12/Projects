import datetime as dt
from random import choice
import smtplib

my_email = "ankurrawatc6rcitt@gmail.com"
password = "b(O3eTdsH8##g"
now = dt.datetime.now()
weekday = now.weekday()

if weekday:
    with open("quotes.txt") as data:
        quotes = data.readlines()
        Message = choice(quotes)

    with smtplib.SMTP("smtp.gmail.com", port=80) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="ankurrawat620@gmail.com",
                            msg=f"Subject:Motivational Quote\n\n{Message}"
                            )
