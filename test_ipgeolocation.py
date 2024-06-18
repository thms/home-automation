import unittest
import http.client
import json
from dotenv import load_dotenv
import os

class TestIPGeolocation(unittest.TestCase):

    # runs once before all tests
    @classmethod
    def setUpClass(cls):
        cls.connection = http.client.HTTPSConnection("api.ipgeolocation.io")
        load_dotenv()
        cls.api_key = os.getenv("IPGEOLOCATION_APIKEY")


    def test_get_data(self):
        self.connection.request("GET", f"/astronomy?apiKey={self.api_key}&location=London,GB")
        response = self.connection.getresponse().read()
        data = json.loads(response.decode("utf-8"))
        print(data)
        self.assertEqual("London,GB", data['location']['location'])
        
if __name__ == '__main__':
    unittest.main()