# /// script
# requires-python = ">=3.10"
# dependencies = ["pandas", "matplotlib"]
# ///
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def main():
    data_path = Path("data/oslo_3day_forecast.csv")
    df = pd.read_csv(data_path)

    # 时间转datetime
    df["time"] = pd.to_datetime(df["time"])

    # 绘图
    plt.figure(figsize=(12, 5))
    plt.plot(df["time"], df["temperature_2m"], color="#1f77b4", linewidth=2)
    plt.title("Oslo 3-Day Hourly Temperature Forecast (metno_seamless)", fontsize=14)
    plt.xlabel("Time")
    plt.ylabel("2m Temperature (°C)")
    plt.grid(alpha=0.3)
    plt.xticks(rotation=30)
    plt.tight_layout()

    # 输出图片
    out_dir = Path("out")
    out_dir.mkdir(exist_ok=True)
    plt.savefig(out_dir / "oslo_temperature.png", dpi=300)
    plt.show()
    print("图表已保存到 out/oslo_temperature.png")

if __name__ == "__main__":
    main()

