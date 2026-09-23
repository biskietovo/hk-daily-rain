# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///
import requests
import json
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)
OUT_FILE = DATA / "weather_data.json"

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.91,
    "longitude": 10.75,
    "hourly": "temperature_2m",
    "models": "metno_seamless",
    "forecast_days": 3
}

resp = requests.get(url, params=params)
resp.raise_for_status()
data = resp.json()

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
