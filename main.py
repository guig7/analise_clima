from classe import Metereologia
from data.api import pegar_dados

df = pegar_dados(-23.55, -46.63)

dados_climaticos = Metereologia(
    list(df['time']),
    list(df['temperature_2m_max']),
    list(df['temperature_2m_min']),
    list(df['apparent_temperature_max']),
    list(df['apparent_temperature_min']),
    list(df['wind_speed_10m_max']),
    list(df['uv_index_max'])
)


dados_climaticos.mostrar_dados()