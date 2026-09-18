# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

import requests
import json
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)
FILE = DATA / "hk-hourly-rain.json"

# 香港天文台API，逐小时雨量
URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

if not FILE.exists():
    print("Fetching rainfall data...")
    r = requests.get(URL, headers={"User-Agent": "pfad-assignment2"})
    r.raise_for_status()
    FILE.write_text(r.text, encoding="utf-8")
    print(f"Saved raw data to {FILE}")
else:
    print("Raw file already exists, skip fetch")


raw = json.loads(FILE.read_text(encoding="utf-8"))
print(raw["rainfall"][0])
