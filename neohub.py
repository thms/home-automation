import asyncio
import neohubapi.neohub as neohub
import time
from models.heating_entry import HeatingEntry
from dotenv import load_dotenv
import os

async def run():
    load_dotenv()
    token = os.getenv("NEOHUB_TOKEN")
    hub = neohub.NeoHub(port=4243, token=token)
    hub_data, devices = await hub.get_live_data()
    for device in devices['thermostats']:
        # print(f"Temperature in zone {device.name}: {device.temperature}")
        heating_entry = HeatingEntry({
            'device_id': device.device_id,
            'device_type': 'thermostat',
            'heat_on': device.heat_on,
            'low_battery': device.low_battery,
            'name': device.name,
            'offline': device.offline,
            'target_temperature': device.target_temperature,
            'temperature': device.temperature,
            'created_at': int(time.time()),
        })
        print(heating_entry)
        result = heating_entry.save()
        print(result)

    for device in devices['timeclocks']:
        # print(f"Temperature in zone {device.name}: {device.temperature}")
        heating_entry = HeatingEntry({
            'device_id': device.device_id,
            'device_type': 'timeclock',
            'heat_on': device.heat_on,
            'low_battery': device.low_battery,
            'name': device.name,
            'offline': device.offline,
            'target_temperature': device.target_temperature,
            'temperature': device.temperature,
            'created_at': int(time.time()),
        })
        print(heating_entry)
        result = heating_entry.save()
        print(result)

asyncio.run(run())