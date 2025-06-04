#!/usr/bin/env python3
import requests, json
from rich import print_json

# L'URL reste la même car elle demande déjà toutes les données
url = "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m,precipitation,precipitation_probability,wind_speed_10m&past_days=14"
data = requests.get(url).json()

output_data = []
data_hourly = data['hourly']

for a, b, c, d in zip(
    data_hourly['time'],
    data_hourly['temperature_2m'],
    data_hourly['wind_speed_10m'],
    data_hourly['precipitation_probability'],
):
    point = {
        "timestamp": a,
        "temperature_2m": b,
        "wind_speed_10m": c,
        "precipitation_probability": d,
    }
    output_data.append(point)

# On affiche le JSON final
print_json(json.dumps(output_data))