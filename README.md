# 🌤️ Weather Tracker — Los Angeles

> Automated daily weather data collection using GitHub Actions.
> Every commit is real data, every green square is a real run.

## Latest Reading

| Metric | Value |
|--------|-------|
| **Date** | 2026-09-08 |
| **Conditions** | Partly cloudy ⛅ |
| **Temperature** | 85.7°F (feels like 88.9°F) |
| **High / Low** | 90.0°F / 71.7°F |
| **Humidity** | 53% |
| **Wind** | 7.2 mph |
| **UV Index** | 6.9 |
| **Sunrise** | 2026-09-07T06:30 |
| **Sunset** | 2026-09-07T19:10 |

## About This Project

This project automatically collects daily weather data for Los Angeles using:

- **Python** for data collection and processing
- **Open-Meteo API** for free weather data (no API key needed)
- **GitHub Actions** for scheduled automation
- **CSV + JSON** for data storage

### Data collected: 163 days

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
