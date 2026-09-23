# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "pandas"]
# ///
import requests
import pandas as pd
from pathlib import Path

# 奥斯陆坐标，3天预报，metno_seamless模型
URL = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 59.91,
    "longitude": 10.75,
    "hourly": "temperature_2m",
    "models": "metno_seamless",
    "forecast_days": 3
}

def main():
    # 创建data文件夹
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    resp = requests.get(URL, params=params)
    resp.raise_for_status()
    data = resp.json()

    # 提取时间与温度
    hourly_data = data["hourly"]
    df = pd.DataFrame({
        "time": hourly_data["time"],
        "temperature_2m": hourly_data["temperature_2m"]
    })

    # 保存csv
    out_path = data_dir / "oslo_3day_forecast.csv"
    df.to_csv(out_path, index=False, encoding="utf-8")
    print(f"数据已保存至 {out_path}")
    print(df.head())

if __name__ == "__main__":
    main()

