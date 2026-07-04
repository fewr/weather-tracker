# 🌤️ Weather Tracker — Los Angeles

> Automated daily weather data collection using GitHub Actions.
> Every commit is real data, every green square is a real run.

## Latest Reading

| Metric | Value |
|--------|-------|
| **Date** | 2026-07-04 |
| **Conditions** | Mainly clear 🌤️ |
| **Temperature** | 60.1°F (feels like 61.6°F) |
| **High / Low** | 82.1°F / 56.1°F |
| **Humidity** | 87% |
| **Wind** | 1.0 mph |
| **UV Index** | 8.2 |
| **Sunrise** | 2026-07-04T05:46 |
| **Sunset** | 2026-07-04T20:08 |

## About This Project

This project automatically collects daily weather data for Los Angeles using:

- **Python** for data collection and processing
- **Open-Meteo API** for free weather data (no API key needed)
- **GitHub Actions** for scheduled automation
- **CSV + JSON** for data storage

### Data collected: 97 days

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
