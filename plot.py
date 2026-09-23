# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///
import json
import matplotlib.pyplot as plt
from pathlib import Path

DATA = Path("data")
IN_FILE = DATA / "weather_data.json"
OUT_FILE = Path("out") / "weather_plot.png"

Path("out").mkdir(exist_ok=True)

with open(IN_FILE, "r", encoding="utf-8") as f:
    raw = json.load(f)

time_list = raw["hourly"]["time"]
temp_list = raw["hourly"]["temperature_2m"]

lat = raw["latitude"]
lon = raw["longitude"]
used_model = raw.get("model", "Unknown Model")
start_time = time_list[0]
end_time = time_list[-1]

plt.figure(figsize=(16,6))
plt.plot(time_list, temp_list, linewidth=2)

# ✅自动拼接标题：坐标、模型、时间区间，完全跟着返回的数据走
auto_title = f"Weather Forecast | Lat:{lat:.2f}, Lon:{lon:.2f} | Model:{used_model} | Period: {start_time} ~ {end_time}"
plt.title(auto_title, fontsize=12)

plt.ylabel("Temperature 2m (°C)", fontsize=12)
plt.xlabel("Datetime", fontsize=12)
plt.xticks(time_list[::4], rotation=45, ha="right")
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig(OUT_FILE)
plt.close()

