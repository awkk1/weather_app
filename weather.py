import requests

def get_weather(city, latitude, longitude):
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,apparent_temperature"
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()
    except requests.exceptions.HTTPError:
        print(f"Weather request failed: HTTP {response.status_code}.")
    except requests.exceptions.Timeout:
        print("Weather request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("Weather request failed: could not connect to Open-Meteo.")
    except requests.exceptions.JSONDecodeError:
        print("Weather request failed: Open-Meteo returned invalid JSON.")
    except requests.exceptions.RequestException as e:
        print(f"Weather request failed: {str(e)[:160]}")
    else:

        if not isinstance(data, dict):
            print('Weather request failed: expected a JSON object.')
            return None

        current = data.get("current")

        if not isinstance(current, dict):
            print("Weather request failed: 'current' must be an object.")
            return None

        keys = ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "apparent_temperature"]

        for key in keys:
            if key not in current:
                print(f'Weather request failed: missing field {key}.')
                return None

            if type(current[key]) not in (int, float):
                print(f'Weather request failed: field {key} must be a number.')
                return None

        temperature = current["temperature_2m"]
        relative_humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        apparent_temperature = current["apparent_temperature"]

        return city, temperature, relative_humidity, wind_speed, apparent_temperature