import requests
import datetime as df

pixela_endpoint = "https://pixe.la/v1/users"
token = "hreogjbvdnoudfbgersf"
user_name = "ankurrawat"
graph_id = "graph1"

user_params = {
    "token": token,
    "username": "ankurrawat",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)
# date_now = (df.datetime.now().date())
# today_Date = date_now.replace("-", ""))
date_now = df.datetime.now()
today_date = date_now.strftime("%Y%m%d")
graph_endpoint = f"{pixela_endpoint}/{user_name}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": token
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# # response.raise_for_status()
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{user_name}/graphs/{graph_id}"
user_date = "20210609"
pixel_data = {
    "date": today_date,
    "quantity": input("how many hours did you code today? ")
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_creation_endpoint}/{user_date}"

# response = requests.delete(url=delete_endpoint, headers=headers)
# response.raise_for_status()
# print(response.text)

pixel_update_endpoint = f"{pixel_creation_endpoint}/{today_date}"

new_pixel_data = {
    "quantity": "2.48"
}
response = requests.put(url=pixel_update_endpoint, json=new_pixel_data, headers=headers)
response.raise_for_status()
print(response.text)
