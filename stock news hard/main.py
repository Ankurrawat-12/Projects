import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_API_KEY = "CFE2MQL52OY26QCT"
NEWS_API_KEY = "08a8e5561a1f4b8d81aefe7634acee9b "
stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCK_API_KEY
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
account_sid = "ACcfc788399b0fccd4ba87beb4b3f36b1e"
auth_token = "d212959a4d9f3273e3830a5592f4a02c"

response = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
response.raise_for_status()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterdays_data = data_list[0]
yesterdays_closing_price = float(yesterdays_data["4. close"])

day_before_yesterdays_data = data_list[1]
day_before_yesterdays_closing_price = float(day_before_yesterdays_data["4. close"])

difference = yesterdays_closing_price - day_before_yesterdays_closing_price
up_down = None
if difference > 0:
    up_down = "📈"
else:
    up_down = "📉"

diff_percent = (difference / yesterdays_closing_price) * 100

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME
    }
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    news_response.raise_for_status()
    article = news_response.json()["articles"]
    three_articles = article[:3]
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}.\nBrief: {article['description']}"
                          for article in three_articles]

    client = Client(account_sid, auth_token)
    for article in formatted_articles:
        message = client.messages \
            .create(
                body=article,
                from_="+16468330538",
                to="+918287413412"
            )
        print(message.status)
