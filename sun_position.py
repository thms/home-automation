import http.client
import json
import time
from models.sun_position import SunPosition
from dotenv import load_dotenv
import os


def main():
    # Get the current position of the sun
    load_dotenv()
    api_key = os.getenv("IPGEOLOCATION_APIKEY")
    connection = http.client.HTTPSConnection("api.ipgeolocation.io")
    connection.request("GET", f"/astronomy?apiKey={api_key}&location=London,GB")
    response = connection.getresponse().read()
    data = json.loads(response.decode("utf-8"))
    connection.close()

    # Store in database
    # Note: this must be in the order it is defined in the database schema, not an arbitrary dict
    sun_position = SunPosition({
        'altitude': data["sun_altitude"],
        'azimuth': data["sun_azimuth"],
        'sunrise': data["sunrise"],
        'sunset': data["sunset"],
        'created_at': int(time.time())
    })
    print(sun_position)
    result = sun_position.save()
    print(result)

main()