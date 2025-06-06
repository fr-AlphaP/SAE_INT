import json
from datetime import datetime

#Fonction pour convertir une date ISO. Par exemple : il y aura 6.07 pour 6h07.
def iso_to_hour_concat(iso_str):
    if not iso_str:
        return None
    if len(iso_str) == 16:
        iso_str += ":00"
    dt = datetime.fromisoformat(iso_str)
    return float(f"{dt.hour}.{dt.minute:02d}")

# Récupération de la météo avec le lien de l'API
url = (
    "https://api.open-meteo.com/v1/forecast?latitude=45.626804&longitude=1.036274&daily=sunrise,sunset&hourly=temperature_2m,rain,snowfall,wind_speed_10m,relative_humidity_2m,snow_depth,precipitation,cloud_cover,visibility,soil_moisture_0_to_1cm,soil_temperature_0cm,precipitation_probability,apparent_temperature&timezone=auto&forecast_days=3"
)
data = requests.get(url).json()

# Extraction des données en fonction des horaires
hourly = data.get("hourly", {})
hour_tags = [
    "time",
    "temperature_2m",
    "relative_humidity_2m",
    "apparent_temperature",
    "rain",
    "snowfall",
    "snow_depth",
    "precipitation",
    "cloud_cover",
    "visibility",
    "wind_speed_10m",
    "soil_moisture_0_to_1cm",
    "soil_temperature_0cm",
    "precipitation_probability",
]
hourly_cols = [hourly.get(tag, []) for tag in hour_tags]
hourly_points = [dict(zip(hour_tags, vals)) for vals in zip(*hourly_cols)]

# Extraction des données journalières de sunrise/sunset de l'API
daily = data.get("daily", {})
day_tags = ["time", "sunrise", "sunset"]
daily_cols = [daily.get(tag, []) for tag in day_tags]
daily_points = [dict(zip(day_tags, vals)) for vals in zip(*daily_cols)]
daily_map = {p["time"]: p for p in daily_points}

# Ajout de sunset et sunrise en fonction de l'horaire
output = []
for pt in hourly_points:
    date = pt["time"][:10]
    d = daily_map.get(date)
    if d and d.get("sunrise") and d.get("sunset"):
        sunrise_val = iso_to_hour_concat(d["sunrise"])
        sunset_val = iso_to_hour_concat(d["sunset"])
        if sunrise_val is not None:
            pt["sunrise_hour"] = sunrise_val
        if sunset_val is not None:
            pt["sunset_hour"] = sunset_val
    output.append(pt)

# Impression en JSON plat pour que cela fonctionne avec Telegraf vers InfluxDB
print(json.dumps(output))
