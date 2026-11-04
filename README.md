# Weather App 1.0

A small Python command-line application that finds a location by name and displays its current weather using [Open-Meteo](https://open-meteo.com/).

## Features

- Search for a city and retrieve its coordinates.
- Display temperature, relative humidity, apparent temperature, and wind speed.
- Reject empty input and handle unknown locations.
- Handle HTTP errors, timeouts, connection failures, invalid JSON, and unexpected response structures or field types.

The application uses the first matching location returned by Open-Meteo. Add a country to the search, such as `Paris, France`, to narrow the results.

## Technologies

- Python (tested with Python 3.14.7)
- Requests 2.34.2
- Open-Meteo Geocoding API and Weather Forecast API

## Installation and usage

An internet connection is required. No API key is needed for the public Open-Meteo endpoints used by this project.

Download or clone the project, then open a terminal in its directory.

On Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe main.py
```

On macOS or Linux:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python main.py
```

Enter a city name when prompted. Each run performs one lookup.

## Example

Illustrative output; actual values depend on the location and time:

```text
Input the city: Berlin
Info of city Berlin:

Temperature: 12.3 °C
Humidity: 65 %
Apparent temperature: 10.2 °C
Wind speed: 8.1 km/h
```

## Data source

Weather data is provided by [Open-Meteo](https://open-meteo.com/), with location search through its [Geocoding API](https://open-meteo.com/en/docs/geocoding-api). See the [Weather Forecast API documentation](https://open-meteo.com/en/docs) for weather variables and units. Location data originates from [GeoNames](https://www.geonames.org/).
