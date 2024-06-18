import unittest
import http.client
import json
from dotenv import load_dotenv
import os

class TestWeatherapi(unittest.TestCase):

    # runs once before all tests
    @classmethod
    def setUpClass(cls):
        cls.connection = http.client.HTTPConnection("api.weatherapi.com")
        load_dotenv()
        cls.key = os.getenv("WEATHERAPI_KEY")


    def test_get_data(self):
        self.connection.request("GET", f"/v1/current.json?key={self.key}&q=richmond,uk&aqi=no")
        response = self.connection.getresponse().read()
        data = json.loads(response.decode("utf-8"))
        self.assertEqual("Richmond", data['location']['name'])
        self.assertGreater(50, data['current']['temp_c'])
        self.assertIn(data['current']['condition']['text'], ['Sunny', 'Cloudy', 'Partly cloudy'])
        # Cloud cover in percent
        self.assertIn(data['current']['cloud'], [*range(0,101)])
if __name__ == '__main__':
    unittest.main()