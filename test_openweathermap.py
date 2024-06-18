import unittest
import http.client
import json
from dotenv import load_dotenv
import os

class TestOpenweathermap(unittest.TestCase):

    # runs once before all tests
    @classmethod
    def setUpClass(cls):
        cls.connection = http.client.HTTPConnection("api.openweathermap.org")
        load_dotenv()
        cls.app_id = os.getenv("OPENWEATHERMAP_APPID")


    def test_get_data(self):
        self.connection.request("GET", f"/data/2.5/weather?lat=51.46171&lon=-0.30633&units=metric&appid={self.app_id}")
        response = self.connection.getresponse().read()
        data = json.loads(response.decode("utf-8"))
        self.assertEqual('Richmond', data['name'])
        self.assertGreater(50, data['main']['temp'])
        self.assertIn(data['weather'][0]['main'], ['Drizzle','Rain','Clouds', 'Clear', 'Partly cloudy'])
        # Cloud cover in percent
        self.assertIn(data['clouds']['all'], [*range(0,101)])
if __name__ == '__main__':
    unittest.main()
