# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib", "pandas"]
# ///

import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)
SITE = HERE / "site"
SITE.mkdir(exist_ok=True)

json_path = DATA / "oslo_weather.json"
if not json_path.exists():
    raise FileNotFoundError(f"Missing Oslo weather data: {json_path}. Run 'python fetch.py' first.")

with json_path.open("r", encoding="utf-8") as fh:
    payload = json.load(fh)

hourly = payload.get("hourly", {})
times = hourly.get("time", [])
temperatures = hourly.get("temperature_2m", [])
if not times or not temperatures:
    raise ValueError(f"No forecast records found in {json_path}.")

records = []
for time, value in zip(times, temperatures):
    if value is None:
        continue
    records.append({"time": pd.to_datetime(time), "temperature": float(value)})

if not records:
    raise ValueError(f"Forecast records are present but contain no valid temperatures in {json_path}.")

df = pd.DataFrame(records)

plt.figure(figsize=(14, 8))
plt.plot(df["time"], df["temperature"], marker="o", color="#2a6f7f")
plt.title("Oslo 3-Day Hourly Air Temperature Forecast")
plt.xlabel("Time (UTC)")
plt.ylabel("Temperature (deg C)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig(OUT / "oslo_temperature.png", dpi=150)
plt.savefig(SITE / "oslo_temperature.png", dpi=150)
plt.close()

(SITE / "index.html").write_text(
        """<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Oslo Weather Forecast</title>
</head>
<body>
    <h1>Oslo 3-Day Hourly Air Temperature Forecast</h1>
    <img src="oslo_temperature.png" alt="Oslo hourly temperature forecast">
</body>
</html>
""",
        encoding="utf-8",
)

print(f"Loaded {len(df)} hourly forecast records")
print(f"Temperature range: {df['temperature'].min():.1f} to {df['temperature'].max():.1f} deg C")
print("Saved out/oslo_temperature.png")
print("Saved site/index.html")
