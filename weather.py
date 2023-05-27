import requests

API_URL = "https://api.weatherbit.io/v2.0/current"
API_KEY = "17743af575354951a0641940bd0fd785"

def get_current_weather(city, country):
    params = {
        "city": city,
        "country": country,
        "key": API_KEY,
    }

    response = requests.get(API_URL, params=params)

    try:
        response.raise_for_status()  # Raise an exception for non-200 status codes

        data = response.json()

        if "data" in data:
            weather_data = data["data"][0]
            temperature = weather_data["temp"]
            weather_description = weather_data["weather"]["description"]
            print(f"Current weather in {city}, {country}: Temperature: {temperature}C | Description: {weather_description}")
        else:
            print("Error: Weather data not found.")

    except (requests.exceptions.HTTPError, requests.exceptions.JSONDecodeError) as e:
        print(f"Error fetching weather data: {e}")
    except KeyError:
        print("Error: Invalid JSON response.")

# Start the loop
while True:
    # Prompt user for input or exit to quit
    city = input("Enter the city (or enter exit to quit): ")
    country = input("Enter the country : ")

    if city.lower() == "exit":
        break
    else:
        # Fetch and display current weather
        get_current_weather(city, country)
