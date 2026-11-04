from geocoding import find_city
from weather import get_weather

def main():
    user_input = input("Input the city: ").strip()

    if user_input == "":
        print("Error: City name cannot be empty.")
        return None

    data = find_city(user_input)

    if data is None:
        return None
        
    result = get_weather(*data)

    if result is None:
        return None
    
    city, temp, humidity, wind, aps_temp = result
    print(f"Weather in {city}: \n")
    print(f"Temperature: {temp} °C")
    print(f"Humidity: {humidity} %")
    print(f"Apparent temperature: {aps_temp} °C")
    print(f"Wind speed: {wind} km/h")

if __name__ == "__main__":
    main()