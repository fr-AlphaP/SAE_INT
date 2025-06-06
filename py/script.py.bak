#!/usr/bin/env python3
import requests, json
from rich import print_json

url = "https://api.open-meteo.com/v1/forecast?latitude=45.626804&longitude=1.036274&hourly=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation_probability,precipitation,rain,snowfall,snow_depth,cloud_cover,visibility,wind_speed_10m,soil_temperature_0cm,soil_moisture_0_to_1cm&timezone=auto&past_days=92&forecast_days=14"
data = requests.get(url).json()

output_data = []
data_hourly = data['hourly']

tags = [
    'time', 
    'temperature_2m', 
    'relative_humidity_2m', 
    'apparent_temperature', 
    'rain', 
    'snowfall', 
    'snow_depth', 
    'precipitation', 
    'cloud_cover', 
    'visibility', 
    'wind_speed_10m', 
    'soil_moisture_0_to_1cm', 
    'soil_temperature_0cm', 
    'precipitation_probability'
]

list_of_all_values = []

for value in tags:
    value_list = data_hourly[value]
    # print(value_list)
    list_of_all_values.append(value_list)

zipped_data = zip(*list_of_all_values)

for values in zipped_data:
    # print(tags, values)
    output_data.append(dict(zip(tags, values)))

print_json(json.dumps(output_data))
