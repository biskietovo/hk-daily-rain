# /// script
# requires-python = ">=3.10"
# dependencies = ["matplotlib"]
# ///

from pathlib import Path
import matplotlib.pyplot as plt
import pandas as pd

HERE = Path(__file__).parent
DATA = HERE / "data"
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)

csv_path = DATA / "hko-daily-rain-2025.csv"
df = pd.read_csv(csv_path)

df["date"] = pd.to_datetime(df["Date"], format="%Y-%m-%d")
df["rainfall"] = pd.to_numeric(df["Daily rainfall(mm)", errors="coerce"])

plt.figure(figsize=(14,5)
           plt.bar(df["date"], df["rainfall"], color="#2a6f7f", width=1.0)
           plt.title("Hong Kong Daily Rainfall in 2025 (HKO Observatory)")
           plt.xlabel("Date")
           plt.ylabel("Daily Rainfall (mm)")
           plt.xticks(rotation=45, ha="right")
           plt.tight_layout()
           pkt.savefig(OUT / "plot.png", dpi=150)
           plt.show()

           print(f"Loaded {len(df)} records")
           print(f"Max daily rainfall: {df['rainfall'].max():.2f} mm")
           print("Saved out/plot.png")
