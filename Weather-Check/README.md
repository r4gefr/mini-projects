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
🌡️ Temperature   : 33.4°C
🤒 Feels Like    : 36.1°C
💧 Humidity      : 64%
🌬️ Wind Speed    : 3.8 m/s
☁️ Condition     : Clear Sky
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

## Future Improvements

- 5-day weather forecast
- Air Quality Index (AQI)
- UV Index
- Weather icons
- Search history
- Colored terminal output
- Save favorite cities

---

