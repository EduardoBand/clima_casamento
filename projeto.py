import requests
import pprint

payload = {
    "latitude": -23.75,
    "longitude": -46.45,
    "start_date": "2021-01-01",
    "end_date": "2021-12-31",
    "hourly": "temperature_2m"
}

response=requests.get(url="https://archive-api.open-meteo.com/v1/era5", params=payload).json()
with open("response", "w") as arquivo:
    pprint.pprint(response, arquivo)

