import os
from datetime import datetime

import requests
from dotenv import load_dotenv


# CONFIGURATION

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



# FETCH WEATHER

def get_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=10
        )

        # Invalid API key
        if response.status_code == 401:
            print("\n Invalid API key.")
            return None

        # City not found
        if response.status_code == 404:
            print(f"\n Could not find '{city}'.")
            return None

        # API rate limit
        if response.status_code == 429:
            print("\n Too many requests. Please try again later.")
            return None

        response.raise_for_status()

        return response.json()

    except requests.exceptions.ConnectionError:
        print("\n No internet connection.")
        return None

    except requests.exceptions.Timeout:
        print("\n Request timed out.")
        return None

    except requests.exceptions.RequestException as e:
        print(f"\n Request error: {e}")
        return None


# DISPLAY WEATHER

def display_weather(data):

    sunrise = datetime.fromtimestamp(
        data["sys"]["sunrise"]
    ).strftime("%I:%M %p")

    sunset = datetime.fromtimestamp(
        data["sys"]["sunset"]
    ).strftime("%I:%M %p")

    print("\n" + "=" * 55)
    print("                  WEATHER REPORT")
    print("=" * 55)

    print(f"📍 Location      : {data['name']}, {data['sys']['country']}")
    print(f"🌡️  Temperature   : {data['main']['temp']:.1f}°C")
    print(f"🤒 Feels Like    : {data['main']['feels_like']:.1f}°C")
    print(f"☁️  Condition     : {data['weather'][0]['description'].title()}")
    print(f"💧 Humidity      : {data['main']['humidity']}%")
    print(f"🌬️  Wind Speed    : {data['wind']['speed']} m/s")
    print(f"🎯 Pressure      : {data['main']['pressure']} hPa")
    print(f"👀 Visibility    : {data['visibility'] / 1000:.1f} km")
    print(f"🌅 Sunrise       : {sunrise}")
    print(f"🌇 Sunset        : {sunset}")

    print("=" * 55)


# MAIN

def main():
    
    if not API_KEY:
        print("\n API_KEY not found in .env file.")
        return

    print("=" * 55)
    print("                  WEATHER CLI")
    print("=" * 55)

    while True:

        city = input(
            "\n Enter city name (or 'exit' to quit): "
        ).strip()
        
        # Exit
        if city.lower() == "exit":
            print("\n Thanks for using Weather CLI!")
            break

        # Empty input
        if not city:
            print("\n  Please enter a city name.")
            continue

        print("\n Fetching weather data...")

        weather = get_weather(city)

        if weather:
            display_weather(weather)
            

if __name__ == "__main__":
    main()