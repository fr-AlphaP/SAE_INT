#!/usr/bin/env python3
import requests, json
from rich import print_json

url = "https://api.open-meteo.com/v1/forecast?latitude=45.626804&longitude=1.036274&timezone=auto&hourly=wind_speed_10m&forecast_days=1&past_days=1"
data = requests.get(url).json()

output_data = []

for t, ws in zip(data['hourly']['time'], data['hourly']['wind_speed_10m']):
    point = {"timestamp": t, "wind_speed_10m": ws}
    output_data.append(point)
print_json(json.dumps(output_data))