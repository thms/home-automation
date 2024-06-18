import unittest
import neohubapi.neohub as neohub
from dotenv import load_dotenv
import os


class TestNeohub(unittest.IsolatedAsyncioTestCase):

    # runs once before all tests
    async def asyncSetUp(self):
        load_dotenv()
        self.token = os.getenv('NEOHUB_TOKEN')
        self.hub = neohub.NeoHub(port=4243, token=self.token)
        self.hub_data, self.devices = await self.hub.get_live_data()



    async def test_get_data(self):
        for device in self.devices['timeclocks']:
            print(device)
            self.assertIn(device.name, ["Charlie", "Hot Water"])

if __name__ == '__main__':
    unittest.main()