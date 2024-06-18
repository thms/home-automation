import http.client
import json
import time
from models.weather import Weather
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    app_id = os.getenv("OPENWEATHERMAP_APPID")
    # Get the current weather data from openweathermap
    connection = http.client.HTTPConnection("api.openweathermap.org")
    connection.request('GET', f'/data/2.5/weather?lat=51.46171&lon=-0.30633&units=metric&appid={app_id}')
    response = connection.getresponse().read()
    data = json.loads(response.decode("utf-8"))
    connection.close()

    # Store in database
    # Note: this must be in the order it is defined in the database schema, not an arbitrary thing
    weather = Weather({
        'temperature': data['main']['temp'],
        'condition': data['weather'][0]['main'],
        'cloud': data['clouds']['all'],
        'created_at': int(time.time()),
        'source': 'openweathermap'
    })
    print(weather)
    result = weather.save()
    print(result)

main()