import os
from datetime import datetime, timezone, timedelta
import tkinter as tk
import tkinter.font as tkfont

import requests
from dotenv import load_dotenv


# ============================================================
# CONFIGURATION
# ============================================================

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# ============================================================
# DESIGN SYSTEM
# ============================================================

BG = "#F5F5F7"
CARD = "#FFFFFF"
TEXT = "#1D1D1F"
SECONDARY = "#6E6E73"
MUTED = "#86868B"
ACCENT = "#0071E3"
ACCENT_DARK = "#0062C4"
SUCCESS = "#248A3D"
ERROR = "#D70015"
BORDER = "#E5E5E7"
SOFT_BLUE = "#F0F6FF"


# ============================================================
# FONT SELECTION
# ============================================================

def get_best_font():

    available_fonts = set(tkfont.families())

    preferred_fonts = [
        "SF Pro Display",
        "SF Pro",
        "Helvetica Neue",
        "Helvetica",
        "Poppins",
        "Segoe UI"
    ]

    for font in preferred_fonts:
        if font in available_fonts:
            return font

    return "Arial"


# ============================================================
# WEATHER API
# ============================================================

def get_weather(city):
    """Fetch weather information from OpenWeatherMap."""

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

        if response.status_code == 401:
            return None, "Invalid API key."

        if response.status_code == 404:
            return None, f"Could not find '{city}'."

        if response.status_code == 429:
            return None, "Too many requests. Please try again later."

        response.raise_for_status()

        return response.json(), None

    except requests.exceptions.ConnectionError:
        return None, "No internet connection."

    except requests.exceptions.Timeout:
        return None, "Request timed out."

    except requests.exceptions.RequestException as e:
        return None, f"Request error: {e}"


# ============================================================
# WEATHER ICON
# ============================================================

def get_weather_icon(weather_id):
    """Return an emoji based on OpenWeatherMap weather ID."""

    if 200 <= weather_id < 300:
        return "⛈"

    elif 300 <= weather_id < 400:
        return "🌦"

    elif 500 <= weather_id < 600:
        return "🌧"

    elif 600 <= weather_id < 700:
        return "❄"

    elif 700 <= weather_id < 800:
        return "🌫"

    elif weather_id == 800:
        return "☀"

    elif 801 <= weather_id <= 804:
        return "☁"

    return "🌡"


# ============================================================
# WIND DIRECTION
# ============================================================

def get_wind_direction(degrees):

    directions = [
        "N",
        "NE",
        "E",
        "SE",
        "S",
        "SW",
        "W",
        "NW"
    ]

    index = round(degrees / 45) % 8

    return directions[index]


# ============================================================
# MAIN APPLICATION
# ============================================================

class WeatherApp:

    def __init__(self, root):

        self.root = root

        self.font = get_best_font()

        self.root.title("WeatherCheck")
        self.root.geometry("820x760")
        self.root.minsize(760, 700)
        self.root.configure(bg=BG)

        self.create_interface()

    # ========================================================
    # INTERFACE
    # ========================================================

    def create_interface(self):

        # ----------------------------------------------------
        # MAIN CONTAINER
        # ----------------------------------------------------

        self.main = tk.Frame(
            self.root,
            bg=BG
        )

        self.main.pack(
            fill="both",
            expand=True,
            padx=55,
            pady=42
        )

        # ----------------------------------------------------
        # HEADER
        # ----------------------------------------------------

        header = tk.Frame(
            self.main,
            bg=BG
        )

        header.pack(
            fill="x"
        )

        title = tk.Label(
            header,
            text="WeatherCheck",
            font=(self.font, 28, "bold"),
            bg=BG,
            fg=TEXT
        )

        title.pack(
            anchor="w"
        )

        subtitle = tk.Label(
            header,
            text="Real-time weather, beautifully presented.",
            font=(self.font, 11),
            bg=BG,
            fg=SECONDARY
        )

        subtitle.pack(
            anchor="w",
            pady=(5, 0)
        )

        # ----------------------------------------------------
        # SEARCH BAR
        # ----------------------------------------------------

        search_container = tk.Frame(
            self.main,
            bg=BG
        )

        search_container.pack(
            fill="x",
            pady=(32, 25)
        )

        self.search_box = tk.Frame(
            search_container,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        self.search_box.pack(
            fill="x"
        )

        search_icon = tk.Label(
            self.search_box,
            text="⌕",
            font=(self.font, 20),
            bg=CARD,
            fg=MUTED
        )

        search_icon.pack(
            side="left",
            padx=(18, 8)
        )

        self.city_entry = tk.Entry(
            self.search_box,
            font=(self.font, 12),
            bg=CARD,
            fg=TEXT,
            insertbackground=TEXT,
            relief="flat",
            borderwidth=0
        )

        self.city_entry.pack(
            side="left",
            fill="x",
            expand=True,
            ipady=13
        )

        self.city_entry.insert(
            0,
            "Search for a city"
        )

        self.city_entry.config(
            fg=MUTED
        )

        self.city_entry.bind(
            "<FocusIn>",
            self.clear_placeholder
        )

        self.city_entry.bind(
            "<FocusOut>",
            self.restore_placeholder
        )

        self.city_entry.bind(
            "<Return>",
            lambda event: self.search_weather()
        )

        self.search_button = tk.Button(
            self.search_box,
            text="Search",
            command=self.search_weather,
            font=(self.font, 10, "bold"),
            bg=ACCENT,
            fg="white",
            activebackground=ACCENT_DARK,
            activeforeground="white",
            relief="flat",
            borderwidth=0,
            cursor="hand2",
            padx=23,
            pady=10
        )

        self.search_button.pack(
            side="right",
            padx=8
        )

        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        self.status_label = tk.Label(
            self.main,
            text="",
            font=(self.font, 9),
            bg=BG,
            fg=SECONDARY
        )

        self.status_label.pack(
            anchor="w",
            pady=(0, 14)
        )

        # ----------------------------------------------------
        # HERO CARD
        # ----------------------------------------------------

        self.hero_card = tk.Frame(
            self.main,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        self.hero_card.pack(
            fill="x"
        )

        # Top section
        hero_top = tk.Frame(
            self.hero_card,
            bg=CARD
        )

        hero_top.pack(
            fill="x",
            padx=35,
            pady=(30, 0)
        )

        self.location_label = tk.Label(
            hero_top,
            text="—",
            font=(self.font, 18, "bold"),
            bg=CARD,
            fg=TEXT
        )

        self.location_label.pack(
            anchor="w"
        )

        self.time_label = tk.Label(
            hero_top,
            text="",
            font=(self.font, 10),
            bg=CARD,
            fg=MUTED
        )

        self.time_label.pack(
            anchor="w",
            pady=(3, 0)
        )

        # Main weather display
        weather_main = tk.Frame(
            self.hero_card,
            bg=CARD
        )

        weather_main.pack(
            fill="x",
            padx=35,
            pady=(15, 25)
        )

        self.icon_label = tk.Label(
            weather_main,
            text="☀",
            font=("Segoe UI Symbol", 58),
            bg=CARD,
            fg="#F5B700"
        )

        self.icon_label.pack(
            side="left",
            padx=(5, 22)
        )

        temperature_section = tk.Frame(
            weather_main,
            bg=CARD
        )

        temperature_section.pack(
            side="left"
        )

        self.temperature_label = tk.Label(
            temperature_section,
            text="--°",
            font=(self.font, 58, "bold"),
            bg=CARD,
            fg=TEXT
        )

        self.temperature_label.pack(
            anchor="w"
        )

        self.condition_label = tk.Label(
            temperature_section,
            text="",
            font=(self.font, 13),
            bg=CARD,
            fg=SECONDARY
        )

        self.condition_label.pack(
            anchor="w",
            pady=(0, 4)
        )

        self.feels_main_label = tk.Label(
            temperature_section,
            text="",
            font=(self.font, 10),
            bg=CARD,
            fg=MUTED
        )

        self.feels_main_label.pack(
            anchor="w"
        )

        # ----------------------------------------------------
        # METRICS
        # ----------------------------------------------------

        metrics = tk.Frame(
            self.main,
            bg=BG
        )

        metrics.pack(
            fill="x",
            pady=(18, 0)
        )

        self.humidity = self.create_metric(
            metrics,
            "Humidity",
            "—",
            "💧"
        )

        self.wind = self.create_metric(
            metrics,
            "Wind",
            "—",
            "↗"
        )

        self.pressure = self.create_metric(
            metrics,
            "Pressure",
            "—",
            "◉"
        )

        self.visibility = self.create_metric(
            metrics,
            "Visibility",
            "—",
            "◎"
        )

        # ----------------------------------------------------
        # DETAILS
        # ----------------------------------------------------

        details = tk.Frame(
            self.main,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        details.pack(
            fill="x",
            pady=(18, 0)
        )

        details_title = tk.Label(
            details,
            text="Today's details",
            font=(self.font, 12, "bold"),
            bg=CARD,
            fg=TEXT
        )

        details_title.pack(
            anchor="w",
            padx=25,
            pady=(20, 12)
        )

        details_grid = tk.Frame(
            details,
            bg=CARD
        )

        details_grid.pack(
            fill="x",
            padx=25,
            pady=(0, 20)
        )

        self.sunrise = self.create_detail(
            details_grid,
            "Sunrise",
            "—"
        )

        self.sunset = self.create_detail(
            details_grid,
            "Sunset",
            "—"
        )

        self.wind_direction = self.create_detail(
            details_grid,
            "Wind Direction",
            "—"
        )

    # ========================================================
    # METRIC CARD
    # ========================================================

    def create_metric(self, parent, title, value, icon):

        card = tk.Frame(
            parent,
            bg=CARD,
            highlightthickness=1,
            highlightbackground=BORDER
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=4
        )

        icon_label = tk.Label(
            card,
            text=icon,
            font=(self.font, 14),
            bg=CARD,
            fg=ACCENT
        )

        icon_label.pack(
            anchor="w",
            padx=17,
            pady=(15, 3)
        )

        value_label = tk.Label(
            card,
            text=value,
            font=(self.font, 15, "bold"),
            bg=CARD,
            fg=TEXT
        )

        value_label.pack(
            anchor="w",
            padx=17
        )

        title_label = tk.Label(
            card,
            text=title,
            font=(self.font, 9),
            bg=CARD,
            fg=MUTED
        )

        title_label.pack(
            anchor="w",
            padx=17,
            pady=(2, 15)
        )

        return value_label

    # ========================================================
    # DETAIL
    # ========================================================

    def create_detail(self, parent, title, value):

        frame = tk.Frame(
            parent,
            bg=CARD
        )

        frame.pack(
            side="left",
            fill="x",
            expand=True
        )

        title_label = tk.Label(
            frame,
            text=title,
            font=(self.font, 9),
            bg=CARD,
            fg=MUTED
        )

        title_label.pack(
            anchor="w"
        )

        value_label = tk.Label(
            frame,
            text=value,
            font=(self.font, 11, "bold"),
            bg=CARD,
            fg=TEXT
        )

        value_label.pack(
            anchor="w",
            pady=(4, 0)
        )

        return value_label

    # ========================================================
    # PLACEHOLDER
    # ========================================================

    def clear_placeholder(self, event):

        if self.city_entry.get() == "Search for a city":

            self.city_entry.delete(
                0,
                tk.END
            )

            self.city_entry.config(
                fg=TEXT
            )

    def restore_placeholder(self, event):

        if not self.city_entry.get().strip():

            self.city_entry.insert(
                0,
                "Search for a city"
            )

            self.city_entry.config(
                fg=MUTED
            )

    # ========================================================
    # SEARCH
    # ========================================================

    def search_weather(self):

        city = self.city_entry.get().strip()

        if city == "Search for a city":
            city = ""

        if not city:

            self.status_label.config(
                text="Please enter a city name.",
                fg=ERROR
            )

            return

        if not API_KEY:

            self.status_label.config(
                text="API_KEY not found in .env file.",
                fg=ERROR
            )

            return

        self.status_label.config(
            text="Fetching weather...",
            fg=ACCENT
        )

        self.search_button.config(
            state="disabled",
            text="Loading..."
        )

        self.root.update_idletasks()

        data, error = get_weather(city)

        self.search_button.config(
            state="normal",
            text="Search"
        )

        if error:

            self.status_label.config(
                text=error,
                fg=ERROR
            )

            return

        self.display_weather(data)

    # ========================================================
    # DISPLAY WEATHER
    # ========================================================

    def display_weather(self, data):

        weather_id = data["weather"][0]["id"]

        weather_icon = get_weather_icon(
            weather_id
        )

        description = (
            data["weather"][0]["description"]
            .title()
        )

        temperature = data["main"]["temp"]

        feels_like = data["main"]["feels_like"]

        wind_speed = data["wind"]["speed"]

        wind_degrees = data["wind"].get(
            "deg",
            0
        )

        wind_direction = get_wind_direction(
            wind_degrees
        )

        city_timezone = timezone(
            timedelta(
                seconds=data["timezone"]
            )
        )

        local_time = datetime.now(
            timezone.utc
        ).astimezone(
            city_timezone
        ).strftime("%I:%M %p"
        )

        sunrise = datetime.fromtimestamp(
            data["sys"]["sunrise"],
            tz=timezone.utc
        ).astimezone(
            city_timezone
        ).strftime("%I:%M %p"
        )

        sunset = datetime.fromtimestamp(
            data["sys"]["sunset"],
            tz=timezone.utc
        ).astimezone(
            city_timezone
        ).strftime("%I:%M %p"
        )

        # ----------------------------------------------------
        # UPDATE LOCATION
        # ----------------------------------------------------

        self.location_label.config(
            text=f"{data['name']}, {data['sys']['country']}"
        )

        self.time_label.config(
            text=f"Local time  •  {local_time}"
        )

        # ----------------------------------------------------
        # WEATHER
        # ----------------------------------------------------

        self.icon_label.config(
            text=weather_icon
        )

        self.temperature_label.config(
            text=f"{temperature:.1f}°"
        )

        self.condition_label.config(
            text=description
        )

        self.feels_main_label.config(
            text=f"Feels like {feels_like:.1f}°"
        )

        # ----------------------------------------------------
        # METRICS
        # ----------------------------------------------------

        self.humidity.config(
            text=f"{data['main']['humidity']}%"
        )

        self.wind.config(
            text=f"{wind_speed:.1f} m/s"
        )

        self.pressure.config(
            text=f"{data['main']['pressure']} hPa"
        )

        visibility = data.get(
            "visibility",
            0
        ) / 1000

        self.visibility.config(
            text=f"{visibility:.1f} km"
        )

        # ----------------------------------------------------
        # DETAILS
        # ----------------------------------------------------

        self.sunrise.config(
            text=sunrise
        )

        self.sunset.config(
            text=sunset
        )

        self.wind_direction.config(
            text=wind_direction
        )

        # ----------------------------------------------------
        # STATUS
        # ----------------------------------------------------

        self.status_label.config(
            text="Weather updated successfully",
            fg=SUCCESS
        )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = WeatherApp(root)

    root.mainloop()