"""
Weather Data Tracker
====================
Fetches daily weather data from the Open-Meteo API (free, no API key needed)
and saves it as a daily JSON snapshot + appends to a running CSV log.

This runs automatically via GitHub Actions every day at 8am UTC.
Every run = a real commit on your GitHub contribution graph.
"""

import json
import csv
import os
from datetime import datetime, timezone
from urllib.request import urlopen, Request
from urllib.error import URLError

# ── Configuration ──────────────────────────────────────────────
# Change these to track a different city!
# Find coordinates at: https://www.latlong.net/
CITY_NAME = "Los Angeles"
LATITUDE = 34.05
LONGITUDE = -118.24

API_URL = (
    f"https://api.open-meteo.com/v1/forecast?"
    f"latitude={LATITUDE}&longitude={LONGITUDE}"
    f"&current=temperature_2m,relative_humidity_2m,wind_speed_10m,"
    f"apparent_temperature,precipitation,weather_code"
    f"&daily=temperature_2m_max,temperature_2m_min,precipitation_sum,"
    f"sunrise,sunset,uv_index_max"
    f"&temperature_unit=fahrenheit"
    f"&wind_speed_unit=mph"
    f"&precipitation_unit=inch"
    f"&timezone=America/Los_Angeles"
)

DATA_DIR = "data"
DAILY_DIR = os.path.join(DATA_DIR, "daily")
LOG_FILE = os.path.join(DATA_DIR, "weather_log.csv")


def fetch_weather():
    """Fetch current weather data from Open-Meteo API."""
    print(f"Fetching weather for {CITY_NAME}...")
    req = Request(API_URL, headers={"User-Agent": "WeatherTracker/1.0"})

    try:
        with urlopen(req, timeout=30) as response:
            data = json.loads(response.read().decode())
        print("  ✓ Data received successfully")
        return data
    except URLError as e:
        print(f"  ✗ Failed to fetch data: {e}")
        raise


def process_data(raw_data):
    """Extract the fields we care about into a clean dict."""
    now = datetime.now(timezone.utc)
    current = raw_data.get("current", {})
    daily = raw_data.get("daily", {})

    processed = {
        "timestamp": now.isoformat(),
        "date": now.strftime("%Y-%m-%d"),
        "city": CITY_NAME,
        "latitude": LATITUDE,
        "longitude": LONGITUDE,
        # Current conditions
        "temperature_f": current.get("temperature_2m"),
        "feels_like_f": current.get("apparent_temperature"),
        "humidity_pct": current.get("relative_humidity_2m"),
        "wind_speed_mph": current.get("wind_speed_10m"),
        "precipitation_in": current.get("precipitation"),
        "weather_code": current.get("weather_code"),
        # Daily summary (today = index 0)
        "high_f": daily.get("temperature_2m_max", [None])[0],
        "low_f": daily.get("temperature_2m_min", [None])[0],
        "total_precip_in": daily.get("precipitation_sum", [None])[0],
        "uv_index_max": daily.get("uv_index_max", [None])[0],
        "sunrise": daily.get("sunrise", [None])[0],
        "sunset": daily.get("sunset", [None])[0],
    }

    return processed


def save_daily_snapshot(data):
    """Save today's data as a standalone JSON file."""
    os.makedirs(DAILY_DIR, exist_ok=True)
    filename = os.path.join(DAILY_DIR, f"{data['date']}.json")

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"  ✓ Saved snapshot: {filename}")
    return filename


def append_to_log(data):
    """Append today's data as a row in the running CSV log."""
    os.makedirs(DATA_DIR, exist_ok=True)
    file_exists = os.path.exists(LOG_FILE)

    fieldnames = [
        "date", "city", "temperature_f", "feels_like_f", "high_f", "low_f",
        "humidity_pct", "wind_speed_mph", "precipitation_in",
        "total_precip_in", "uv_index_max", "weather_code",
        "sunrise", "sunset", "timestamp"
    ]

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        # Only write the fields we want in the CSV
        row = {k: data.get(k) for k in fieldnames}
        writer.writerow(row)

    print(f"  ✓ Appended to log: {LOG_FILE}")


def update_readme(data):
    """Update README.md with the latest weather reading."""
    weather_descriptions = {
        0: "Clear sky ☀️",
        1: "Mainly clear 🌤️", 2: "Partly cloudy ⛅", 3: "Overcast ☁️",
        45: "Foggy 🌫️", 48: "Depositing rime fog 🌫️",
        51: "Light drizzle 🌦️", 53: "Moderate drizzle 🌦️", 55: "Dense drizzle 🌧️",
        61: "Slight rain 🌧️", 63: "Moderate rain 🌧️", 65: "Heavy rain 🌧️",
        71: "Slight snow ❄️", 73: "Moderate snow ❄️", 75: "Heavy snow ❄️",
        80: "Slight showers 🌦️", 81: "Moderate showers 🌦️", 82: "Violent showers ⛈️",
        95: "Thunderstorm ⛈️", 96: "Thunderstorm with hail ⛈️",
    }

    code = data.get("weather_code", 0)
    description = weather_descriptions.get(code, f"Code {code}")

    # Count how many days of data we have
    daily_files = []
    if os.path.exists(DAILY_DIR):
        daily_files = [f for f in os.listdir(DAILY_DIR) if f.endswith(".json")]

    readme = f"""# 🌤️ Weather Tracker — {CITY_NAME}

> Automated daily weather data collection using GitHub Actions.
> Every commit is real data, every green square is a real run.

## Latest Reading

| Metric | Value |
|--------|-------|
| **Date** | {data['date']} |
| **Conditions** | {description} |
| **Temperature** | {data['temperature_f']}°F (feels like {data['feels_like_f']}°F) |
| **High / Low** | {data['high_f']}°F / {data['low_f']}°F |
| **Humidity** | {data['humidity_pct']}% |
| **Wind** | {data['wind_speed_mph']} mph |
| **UV Index** | {data['uv_index_max']} |
| **Sunrise** | {data['sunrise']} |
| **Sunset** | {data['sunset']} |

## About This Project

This project automatically collects daily weather data for {CITY_NAME} using:

- **Python** for data collection and processing
- **Open-Meteo API** for free weather data (no API key needed)
- **GitHub Actions** for scheduled automation
- **CSV + JSON** for data storage

### Data collected: {len(daily_files)} days

All data lives in the `data/` directory:
- `data/daily/` — One JSON file per day
- `data/weather_log.csv` — Running CSV log of all readings

## How It Works

1. GitHub Actions runs `collect.py` every day at 8:00 AM UTC
2. The script fetches current weather from the Open-Meteo API
3. Data is saved as a daily JSON snapshot and appended to the CSV log
4. Changes are committed and pushed automatically

## Setup Your Own

1. Fork this repo
2. Edit `CITY_NAME`, `LATITUDE`, `LONGITUDE` in `collect.py`
3. That's it — GitHub Actions handles the rest!
"""

    with open("README.md", "w") as f:
        f.write(readme)

    print("  ✓ Updated README.md")


def main():
    print("=" * 50)
    print(f"Weather Tracker — {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")
    print("=" * 50)

    raw_data = fetch_weather()
    processed = process_data(raw_data)

    save_daily_snapshot(processed)
    append_to_log(processed)
    update_readme(processed)

    print()
    print(f"  Current: {processed['temperature_f']}°F, "
          f"High: {processed['high_f']}°F, Low: {processed['low_f']}°F")
    print("=" * 50)
    print("Done! Ready to commit.")


if __name__ == "__main__":
    main()
