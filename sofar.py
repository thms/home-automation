import minimalmodbus
import serial
import time
from sys import exit
from models.solar_entry import SolarEntry 

###		PROGRAM FLOW:
###			- Collect Data from Sofar HYD3000-ES inverter
###			- Convert to values and store in database



### COLLECT DATA FROM SOFAR HYD6000 INVERTER ###

def main():

    instrument = minimalmodbus.Instrument('/dev/serial0', 1) # port name, slave address 

    instrument.serial.baudrate = 9600   # Baud
    instrument.serial.bytesize = 8
    instrument.serial.parity   = serial.PARITY_NONE
    instrument.serial.stopbits = 1
    instrument.serial.timeout  = 0.5   # seconds

    # Interesting data
    try:
        # The four power paths from the display
        grid_power = instrument.read_register(0x212, 2, functioncode=3, signed=True) # read total grid pwr [kW] negative whem consuming from the grid
        pv_power = instrument.read_register(0x215, 2, functioncode=3, signed=False) # read SolarPV Generation Pwr [kW]
        load_power = instrument.read_register(0x213, 2, functioncode=3, signed=False) # read load pwr [kW]
        battery_power = instrument.read_register(0x20d, 2, functioncode=3, signed=True) # read battery charge discharge pwr [kW], negative when consuming from battery

        pv_1_voltage = instrument.read_register(0x250, 1, functioncode=3, signed=False) # PV 1 Voltage [V]
        pv_1_current = instrument.read_register(0x251, 2, functioncode=3, signed=False) # PV 1 current [A]
        pv_1_power = instrument.read_register(0x252, 2, functioncode=3, signed=False) # PV 1 power [kW]

        pv_2_voltage = instrument.read_register(0x253, 1, functioncode=3, signed=False) # PV 1 Voltage [V]
        pv_2_current = instrument.read_register(0x254, 2, functioncode=3, signed=False) # PV 1 current [A]
        pv_2_power = instrument.read_register(0x255, 2, functioncode=3, signed=False) # PV 1 power [kW]

        # Battery stuff
        battery_cycles = instrument.read_register(0x22c, 0, functioncode=3, signed=False) # read times batteries have been cycled [#]
        battery_charge = instrument.read_register(0x210, 0, functioncode=3, signed=False) # read battery charge level [%]
        battery_temperature = instrument.read_register(0X211, 0, functioncode=3, signed=True) # Read Battery Temperature as Signed 16-Bit [C]
        battery_voltage = instrument.read_register(0X20e, 1, functioncode=3, signed=False) # Read Battery voltage as Signed 16-Bit [V]
        battery_current = instrument.read_register(0X20f, 2, functioncode=3, signed=True) # Read Battery current as Signed 16-Bit [A], negative when discharging

        # Energy consumption per day
        today_generated_solar_energy = instrument.read_register(0x218, 2, functioncode=3, signed=False) # read Today's generation [kWh]
        today_sold_solar_energy = instrument.read_register(0x219, 2, functioncode=3, signed=False) # read Today's Generation sold [kWh]
        today_bought_grid_energy = instrument.read_register(0x21a, 2, functioncode=3, signed=False) # read Today's Power bought [kWh]
        today_consumed_energy = instrument.read_register(0x21b, 2, functioncode=3, signed=False) # read Today's consumption bought [kWh]

        # Other data
        # grid_frequency = instrument.read_register(0x20c, 2, functioncode=3, signed=False) # read grid frequency [Hz]
        # input_output_power = instrument.read_register(0x214, 2, functioncode=3, signed=True) # read input / output power pwr [kW]

        # Lifetime consumption and generation
        # total_load_consumption_high_byte = instrument.read_register(0x222, 0, functioncode=3, signed=False) * 0xffff # Total Load Consumption [kWh] HighByte
        # total_load_consumption = total_load_consumption_high_byte + instrument.read_register(0x223, 0, functioncode=3, signed=False) # Total Load Consumption [kWh] LowByte
        # total_generation_high_byte = instrument.read_register(0x21c, 0, functioncode=3, signed=False) * 0xffff # Total generation [kWh] HighByte
        # total_generation = total_generation_high_byte + instrument.read_register(0x21d, 0, functioncode=3, signed=False) # Total generation [kWh] LowByte

        # inverter_internal_temperature = instrument.read_register(0x238, 0, functioncode=3, signed=False) # Inverter Internal Temperature [deg C]
        # inverter_heatsink_temperature = instrument.read_register(0x239, 0, functioncode=3, signed=False) # Inverter Heatsink Temperature [deg C]


    except IOError as e:
        print(F"Error reading from inverter {e}")
        exit(0)

    # Store to database
    solar_entry = SolarEntry({
        'battery_charge': battery_charge,
        'battery_power': battery_power,
        'battery_voltage': battery_voltage,
        'battery_current': battery_current,
        'battery_temperature': battery_temperature,
        'battery_cycles': battery_cycles,
        'pv_1_voltage': pv_1_voltage,
        'pv_1_current': pv_1_current,
        'pv_1_power': pv_1_power,
        'pv_2_voltage': pv_2_voltage,
        'pv_2_current': pv_2_current,
        'pv_2_power': pv_2_power,
        'pv_power': pv_power,
        'grid_power': grid_power,
        'load_power': load_power,
        'today_generated_solar_energy': today_generated_solar_energy,
        'today_sold_solar_energy': today_sold_solar_energy,
        'today_bought_grid_energy': today_bought_grid_energy,
        'today_consumed_energy': today_consumed_energy,
        'created_at': int(time.time()),
    })
    print(solar_entry)
    result = solar_entry.save()
    print(result)

main()

