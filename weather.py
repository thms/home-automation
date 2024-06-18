import http.client
import json
import time
from models.weather import Weather
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    key = os.getenv("WEATHERAPI_KEY")
    # Get the current weather data
    connection = http.client.HTTPConnection("api.weatherapi.com")
    connection.request("GET", f"/v1/current.json?key={key}&q=richmond,uk&aqi=no")
    response = connection.getresponse().read()
    data = json.loads(response.decode("utf-8"))
    connection.close()

    # Store in database
    # Note: this must be in the order it is defined in the database schema, not an arbitrary thing
    weather = Weather({
        'temperature': data["current"]["temp_c"],
        'condition': data["current"]["condition"]["text"],
        'cloud': data["current"]["cloud"],
        'created_at': int(time.time()),
        'source': 'weatherapi'
    })
    print(weather)
    #result = weather.save()
    #print(result)

main()