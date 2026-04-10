# 🌤️ Weather Tracker — Los Angeles

> Automated daily weather data collection using GitHub Actions.
> Every commit is real data, every green square is a real run.

## Latest Reading

| Metric | Value |
|--------|-------|
| **Date** | 2026-04-10 |
| **Conditions** | Overcast ☁️ |
| **Temperature** | 61.1°F (feels like 63.4°F) |
| **High / Low** | 72.1°F / 59.9°F |
| **Humidity** | 89% |
| **Wind** | 0.7 mph |
| **UV Index** | 7.5 |
| **Sunrise** | 2026-04-10T06:27 |
| **Sunset** | 2026-04-10T19:20 |

## About This Project

This project automatically collects daily weather data for Los Angeles using:

- **Python** for data collection and processing
- **Open-Meteo API** for free weather data (no API key needed)
- **GitHub Actions** for scheduled automation
- **CSV + JSON** for data storage

### Data collected: 15 days

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
