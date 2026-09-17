# /// script
# requires-python = ">=3.10"
# dependencies = ["requests"]
# ///

"""
Fetch the numbers once, save the raw reply to data/, and never fetch again.

    uv run fetch.py

Change URL and FILE. The default is the Hong Kong Observatory's daily mean
temperature for 2026, so the template runs before you have touched it and you
can see what a file looks like when it arrives. It is an example, not your
phenomenon: handing it in unchanged is handing in nothing.
"""

from pathlib import Path

import requests

URL = ("https://data.weather.gov.hk/weatherAPI/doc/HKO_Open_Data_API_Documentation.pdf")      # CHANGE ME
FILE = "hko-daily-rain-2025.csv"                          # CHANGE ME: say what it is,
                                                                      # keep the publisher's extension
HERE = Path(__file__).parent
DATA = HERE / "data"


def fetch(url, path):
    """Ask for the file once. If it is already in data/, do nothing."""
    if path.exists():
        print("Fetching HKO 2025 daily rainfall csv...")
        headers = {"User-Agent": "sd5913-assignment2/1.0"}
        r = request.get(URL, headers=headers)
        r.raise_for_status()
        FILE.write_bytes(r.content)
        print(f"Raw data saved to {FILE}"


if __name__ == "__main__":
    fetch(URL, DATA / FILE)
