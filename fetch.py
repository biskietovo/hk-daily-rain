# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
# ]
# ///
import requests
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)
OUT_FILE = DATA / "hk_rain_hourly.json"

URL = "https://data.weather.gov.hk/weatherAPI/opendata/weather.php?dataType=rhrread&lang=en"

if not OUT_FILE.exists():
    print("Fetching HK hourly rainfall data...")
    res = requests.get(URL, headers={"User-Agent": "week03-assignment"})
    res.raise_for_status()
    OUT_FILE.write_text(res.text, encoding="utf-8")
    print(f"Saved raw data into {OUT_FILE}")
else:
    print("Raw file exists, skip fetch.")
