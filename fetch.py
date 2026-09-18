# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

import requests
import json
from pathlib import Path

data_dir = Path("data")
data_dir.mkdir(exist_ok=True)
out_file = data_dir / "hk_hour_rain.json"

url = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"
resp = requests.get(url)
resp.raise_for_status()
raw = resp.json()

with open(out_file, "w", encoding="utf-8") as f:
    json.dump(raw, f, indent=2)

print(f"Raw data saved to {out_file}")

