# 🌤️ Weather Tracker — Los Angeles

> Automated daily weather data collection using GitHub Actions.
## Latest Reading

| Metric | Value |
|--------|-------|
| **Date** | 2026-03-27 |
| **Conditions** | Clear sky ☀️ |
| **Temperature** | 66.0°F (feels like 66.5°F) |
| **High / Low** | 82.3°F / 56.1°F |
| **Humidity** | 78% |
| **Wind** | 5.8 mph |
| **UV Index** | 7.3 |
| **Sunrise** | 2026-03-26T06:47 |
| **Sunset** | 2026-03-26T19:09 |

## About This Project

This project automatically collects daily weather data for Los Angeles using:

- **Python** for data collection and processing
- **Open-Meteo API** for free weather data
- **GitHub Actions** for scheduled automation
- **CSV + JSON** for data storage

### Data collected: 1 days

All data lives in the `data/` directory:
- `data/daily/` — One JSON file per day
- `data/weather_log.csv` — Running CSV log of all readings


## Setup Your Own

1. Fork this repo
2. Edit `CITY_NAME`, `LATITUDE`, `LONGITUDE` in `collect.py`
3. That's it — GitHub Actions handles the rest!
