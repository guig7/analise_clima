from data.api import pegar_dados
from data.cooderndas import df_capitais
from datetime import datetime
import pandas as pd


print('Digite a sigla do estado da capital que deseja analisar: (GO, SP, RJ, etc) ')
estado = input()

print(f'Analisando os dados da capital do estado de {estado} \n')

df = pegar_dados(df_capitais[df_capitais['estado'] == estado]['latitude'].iloc[0], df_capitais[df_capitais['estado'] == estado]['longitude'].iloc[0])


for x in df['time']:
    df_dia = df[df['time'] == x]
    print(f'Dados do dia: {x} \n')
    print(f'No dia {x} a temperatura máxima será de {df_dia["temperature_2m_max"].iloc[0]}°C e a mínima será de {df_dia["temperature_2m_min"].iloc[0]}°C. \n')

    print(f'A temperatura aparente máxima será de {df_dia["apparent_temperature_max"].iloc[0]}°C e a mínima será de {df_dia["apparent_temperature_min"].iloc[0]}°C. \n')
    print(f'A velocidade máxima do vento será de {df_dia["wind_speed_10m_max"].iloc[0]} km/h. \n')
    print(f'O índice UV máximo será de {df_dia["uv_index_max"].iloc[0]}. \n')
    print('---------------------------------\n')
