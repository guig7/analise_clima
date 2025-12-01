import requests
import pandas as pd


def pegar_dados(latitude, longitude):
    url =f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&daily=temperature_2m_max,temperature_2m_min,apparent_temperature_max,apparent_temperature_min,wind_speed_10m_max,sunrise,sunset,daylight_duration,sunshine_duration,uv_index_max&timezone=auto'
    resposta = requests.get(url)
    data = resposta.json()
    df = pd.DataFrame(data['daily'])
    return df