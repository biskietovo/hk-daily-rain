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

rainfall_list = raw["rainfall"]
time_labels = []
rain_values = []
for entry in rainfall_list:
    time_labels.append(entry["endTime"])
    rain_values.append(entry["rainfall"])

plt.figure(figsize=(12,5))
plt.plot(time_labels, rain_values, color="#2374ab", linewidth=2)
plt.title("Hong Kong Hourly Rainfall", fontsize=14)
plt.xlabel("Time")
plt.ylabel("Rainfall (mm)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(OUT_FOLDER / "hk_rain_plot.png")
plt.close()
print("Plot saved to out/hk_rain_plot.png")

