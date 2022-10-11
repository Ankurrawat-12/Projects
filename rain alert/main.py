import requests
from twilio.rest import Client

# import os
# api_key = os.environ["OMP_API_KEY"]
api_key = "4c04333579fe18920b6eb0faad93f659"
url = "https://api.openweathermap.org/data/2.5/onecall"
account_sid = "ACcfc788399b0fccd4ba87beb4b3f36b1e"
auth_token = "d212959a4d9f3273e3830a5592f4a02c"
MY_LAT = 28.699681
MY_LON = 77.219724
# MY_LAT = 31.230391
# MY_LON = 121.473701
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    # "q": "Delhi,India",
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=url, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

rain = False
for hour_data in weather_slice:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        rain = True
if rain:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☂",
            from_="+16468330538",
            to="+918287413412"
        )
    print(message.status)
else:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="It's not  going to rain today. You can go without an ☂",
            from_="+16468330538",
            to="+918287413412"
        )
    print(message.status)
