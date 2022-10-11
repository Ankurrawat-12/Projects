from bs4 import BeautifulSoup
import smtplib
import requests

set_price = 15000
MY_EMAIL = "ankurrawatc6rcitt@gmail.com"
PASSWORD = "b(O3eTdsH8##g"

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
"Accept-Language": "en-US,en;q=0.9"
}
url = "https://www.amazon.in/gp/product/1421525828/ref=ox_sc_saved_title_6?smid=AWKKPKP4FBRXQ&psc=1"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())
price = float(soup.find(name="span", class_="a-size-medium a-color-price inlineBlock-display offer-price "
                                            "a-text-normal price3P").text.replace("₹", "").replace(",", ""))
title = soup.find(name="span", class_="a-size-extra-large").getText()
# print(type(price))
# print(price)
# print(title)
if price < set_price:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        msg = f"Subject:Amazon Price Alert! \n\n {title} is now ₹{set_price} \n {url}".encode('utf-8')
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="ankurrawat620@gmail.com", msg=msg)
