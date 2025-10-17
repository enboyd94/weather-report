import os
import json
import requests
import datetime


def get_weather_data(API_KEY):

    city = "Manhattan"
    base_url = "http://api.weatherstack.com/current"

    params = {
        "access_key": API_KEY,
        "query": city
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    timestamp = datetime.datetime.now(datetime.UTC).strftime("%Y%m%d%H%M%S")

    with open(f"data/weather_{timestamp}.json", "w") as f:
        json.dump(data, f)

    with open(f"logs/weather.log", "a") as log_file:
        log_file.write(f"{timestamp} - Fetched weather data for {city}\n")

    print(data)
    print("Done!")


if __name__ == "__main__":
    get_weather_data(os.getenv("WEATHER_API_KEY"))
