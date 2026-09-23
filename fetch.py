# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
# ]
# ///
import requests
import subprocess
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
DATA.mkdir(exist_ok=True)
OUT_FILE = DATA / "oslo_weather.json"

URL = "https://api.open-meteo.com/v1/forecast?latitude=59.91&longitude=10.75&hourly=temperature_2m&models=metno_seamless&forecast_days=3"

print("Fetching latest Oslo weather data...")
res = requests.get(URL, headers={"User-Agent": "oslo-weather-forecast/1.0"})
res.raise_for_status()
OUT_FILE.write_text(res.text, encoding="utf-8")
print(f"Saved raw data into {OUT_FILE}")

subprocess.run(["uv", "run", "plot.py"], cwd=HERE, check=True)
