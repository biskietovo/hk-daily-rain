# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "matplotlib",
# ]
# ///
import json
import matplotlib.pyplot as plt
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT_FOLDER = HERE / "out"
OUT_FOLDER.mkdir(exist_ok=True)
IN_FILE = DATA / "hk_rain_hourly.json"

with open(IN_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

# HKO rhrread 正确嵌套结构
rain_data = raw["rainfall"]["data"]
record_time = raw["rainfall"]["recordTime"]

station_names = []
rain_values = []
for entry in rain_data:
    station_names.append(entry["place"])
    rain_values.append(entry["value"])

plt.figure(figsize=(12, 6))
plt.bar(station_names, rain_values, color="#2374ab")
plt.title(f"Hong Kong Hourly Rainfall | Time: {record_time}", fontsize=14)
plt.xlabel("Weather Station")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=60, ha="right")
plt.tight_layout()
plt.savefig(OUT_FOLDER / "hk_rain_bar.png")
plt.close()
print("Plot saved to out/hk_rain_bar.png")

