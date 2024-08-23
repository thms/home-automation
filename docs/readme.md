# Home Automation System

This repository contains the code for a home automation system that collects data from various sources, stores it in a database, and provides an API for accessing the data.

## API

The system provides a REST API for accessing the data. The API is documented in the `swagger.yaml` file.

## Data Model

The system uses a SQLite database to store the data. The database schema is defined in the `models` directory.

### Models

* **SunPosition:** Stores the position of the sun at a given time.
* **SolarEntry:** Stores data from the Sofar HYD3000-ES inverter.
* **HeatingEntry:** Stores data from the NeoHub thermostat.
* **Weather:** Stores weather data from OpenWeatherMap and WeatherAPI.

## Business Logic

The system's business logic is implemented in the `lib` directory.

### Components

* **orm_sqlite:** Provides an ORM for interacting with the SQLite database.
* **suncalc:** Calculates the position of the sun at a given time.
* **neohub:** Provides an API for interacting with the NeoHub thermostat.
* **sofar:** Provides an API for interacting with the Sofar HYD3000-ES inverter.
* **weather:** Provides an API for interacting with OpenWeatherMap and WeatherAPI.

## Events Consumed

The system consumes the following events:

* **NeoHub events:** The system subscribes to events from the NeoHub thermostat, such as temperature changes and heating status changes.
* **Sofar events:** The system subscribes to events from the Sofar HYD3000-ES inverter, such as power generation and consumption changes.

## Events Published

The system publishes the following events:

* **Data updates:** The system publishes events when data is updated in the database.

## Usage

To use the system, you will need to:

1. Install the required dependencies.
2. Configure the system settings.
3. Start the system.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Timestamp: 2023-10-26T15:38:12.889572+00:00 
