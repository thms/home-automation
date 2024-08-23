## Home Automation System

This repository contains the code for a home automation system that collects data from various sources, stores it in a database, and provides an API for accessing the data.

### API

The system exposes a REST API for accessing the data. The API is documented in the code comments.

### Data Model

The system uses a SQLite database to store the data. The following tables are used:

* **SunPosition:** Stores the position of the sun at different times of the day.
* **SolarEntry:** Stores data from the Sofar HYD3000-ES inverter.
* **HeatingEntry:** Stores data from the NeoHub thermostat and timeclocks.
* **Weather:** Stores weather data from OpenWeatherMap and WeatherAPI.

### Business Logic

The system's business logic is implemented in the following Python modules:

* **sofar.py:** Collects data from the Sofar HYD3000-ES inverter.
* **neohub.py:** Collects data from the NeoHub thermostat and timeclocks.
* **weather.py:** Collects weather data from OpenWeatherMap and WeatherAPI.
* **sun_position.py:** Calculates the position of the sun at different times of the day.

### Events Consumed

The system consumes the following events:

* **Sofar HYD3000-ES inverter data:** This data is collected via a serial connection.
* **NeoHub thermostat and timeclock data:** This data is collected via an API call.
* **OpenWeatherMap and WeatherAPI weather data:** This data is collected via API calls.

### Events Published

The system publishes the following events:

* **New data is available:** This event is published when new data is collected from any of the sources.

### Repository Structure

```
home-automation
├── lib
│   └── orm_sqlite
│       ├── model.py
│       ├── manager.py
│       ├── database.py
│       └── logger.py
├── models
│   ├── sun_position.py
│   ├── solar_entry.py
│   ├── heating_entry.py
│   └── weather.py
├── test_neohub.py
├── sofar.py
├── neohub.py
├── test_ipgeolocation.py
├── sun_position.py
├── test_openweathermap.py
├── test_weatherapi.py
├── weather.py
└── weather2.py
```

### Usage

To use the system, you will need to install the following Python packages:

* `minimalmodbus`
* `pyserial`
* `neohubapi`
* `requests`
* `sqlite3`

You will also need to configure the system with the following information:

* **Sofar HYD3000-ES inverter serial port:** The serial port that the inverter is connected to.
* **NeoHub API token:** The API token for your NeoHub account.
* **OpenWeatherMap API key:** The API key for your OpenWeatherMap account.
* **WeatherAPI API key:** The API key for your WeatherAPI account.

Once the system is configured, you can start it by running the following command:

```
python main.py
```

The system will then start collecting data from the various sources and storing it in the database. You can then access the data via the REST API.

### Future Work

* Implement a web interface for managing the system.
* Add support for more home automation devices.
* Implement a rule engine for automating tasks based on the collected data.
* Add support for cloud storage.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request.

### License

This project is licensed under the MIT License.