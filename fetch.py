# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

import requests
import json
from pathlib import Path

DATA = Path("data")
DATA.mkdir(exist_ok=True)
OUT_FILE = DATA / "hk_rain_hourly.json"

url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
resp = requests.get(url)
resp.raise_for_status()
data = resp.json()

with open(OUT_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)
