# Weather CLI

A simple command-line weather application built with Python that fetches real-time weather information for any city using the OpenWeatherMap API.

---

## Preview

```text
==========================================
            WEATHER CLI
==========================================

Enter city name: Delhi

==========================================
📍 Location      : Delhi, IN
🌡️ Temperature   : 35.5°C
🤒 Feels Like    : 40.3°C
☁️ Condition     : Scattered Clouds
💧 Humidity      : 75%
🌬️  Wind Speed    : 7 m/s
🎯 Pressure      : 1004 hPa
👀 Visibility    : 10.0 km
🌅 Sunrise       : 06:32 AM
🌇 Sunset        : 07:41 PM
==========================================
```

---

## Features

- Search weather by city name
- Current temperature
- Feels like temperature
- Humidity
- Wind speed
- Weather condition
- Handles invalid city names
- Handles network and timeout errors
- Environment variable support using `.env`

---

## Tech Stack

- Python 3
- Requests
- python-dotenv
- OpenWeatherMap API

---

## Project Structure

```
Weather-CLI/
│
├── app.py
├── README.md
├── .env
├── .gitignore
└── requirements.txt
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/MiniProjects.git
```

Move into the project

```bash
cd MiniProjects
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## API Setup

Create a `.env` file in the project root.

```env
API_KEY=YOUR_OPENWEATHERMAP_API_KEY
```

Get your free API key from:

https://openweathermap.org/api

---

## Run

```bash
python app.py
```

---

## Requirements

```text
requests
python-dotenv
```

---


