import requests

def find_city(city_name):
    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city_name,
        "count": 1
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        response.raise_for_status()

        data = response.json()

    except requests.exceptions.HTTPError:
        print(f"City search failed: HTTP {response.status_code}.")
    except requests.exceptions.Timeout:
        print("City search timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        print("City search failed: could not connect to Open-Meteo.")
    except requests.exceptions.JSONDecodeError:
        print("City search failed: Open-Meteo returned invalid JSON.")
    except requests.exceptions.RequestException as e:
        print(f"City search failed: {str(e)[:160]}")
    else:
        if not isinstance(data, dict):
            print('City search failed: expected a JSON object.')
            return None

        result = data.get("results", [])

        if not isinstance(result, list):
            print("City search failed: 'results' must be a list.")
            return None

        if not result:
            print("City search: no matching location found. Check the name or add a country.")
            return None

        if not isinstance(result[0], dict):
            print('City search failed: expected a location object.')
            return None

        keys = ["name", "latitude", "longitude"]

        for key in keys:
            if key not in result[0]:
                print(f'City search failed: missing field {key}.')
                return None
        
        city = result[0]["name"]

        if not isinstance(city, str) or city.strip() == "":
            print('City search failed: location name must be a non-empty string.')
            return None

        latitude = result[0]["latitude"]
        longitude = result[0]["longitude"]

        if type(latitude) not in (int, float) or type(longitude) not in (int, float):
            print('City search failed: latitude and longitude must be numbers.')
            return None

        return(city, latitude, longitude)
    