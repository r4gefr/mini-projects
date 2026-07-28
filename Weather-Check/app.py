import os
import requests
from dotenv import load_dotenv

# Load API Key
load_dotenv()
API_KEY = os.getenv("API_KEY")
print(API_KEY)

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city."""

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        print("Status Code:", response.status_code)
        print("Response:", response.text)      # <-- Debug

        response.raise_for_status()

        return response.json()

    except requests.exceptions.HTTPError:

        print("\n❌ HTTP Error.")
        return None

    except requests.exceptions.ConnectionError:

        print("\n❌ No internet connection.")
        return None

    except requests.exceptions.Timeout:

        print("\n❌ Request timed out.")
        return None

    except requests.exceptions.RequestException as e:

        print(f"\n❌ Error: {e}")
        return None

def display_weather(data):
    """Display formatted weather information."""

    print("\n" + "=" * 42)
    print("                 WEATHER CLI")
    print("=" * 42)

    print(f"📍 Location      : {data['name']}, {data['sys']['country']}")
    print(f"🌡️ Temperature   : {data['main']['temp']}°C")
    print(f"🤒 Feels Like    : {data['main']['feels_like']}°C")
    print(f"💧 Humidity      : {data['main']['humidity']}%")
    print(f"🌬️ Wind Speed    : {data['wind']['speed']} m/s")
    print(f"☁️ Condition     : {data['weather'][0]['description'].title()}")

    print("=" * 42)


def main():

    print("=" * 42)
    print("                 WEATHER CLI")
    print("=" * 42)

    city = input("\nEnter city name: ").strip()

    weather = get_weather(city)

    if weather:
        display_weather(weather)


if __name__ == "__main__":
    main()