# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

import json
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data")
IN_FILE = DATA / "hk_rain_hourly.json"
OUT_FILE = Path("out") / "plot.png"

Path("out").mkdir(exist_ok=True)

with open(IN_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

districts = []
rain_values = []
for entry in raw["rainfall"]:
    districts.append(entry["place"])
    rain_values.append(entry["value"])

plt.figure(figsize=(14,7))
plt.bar(districts, rain_values)
plt.title("Hong Kong Hourly Rainfall by District")
plt.ylabel("Rainfall (Past 60 mins, mm)")
plt.xlabel("District")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig(OUT_FILE)
plt.close()

