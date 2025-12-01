from data.api import pegar_dados

# for x in df['time']:
#     df_dia = df[df['time'] == x]
#     print(f'Dados do dia: {x} \n')
#     print(f'No dia {x} a temperatura máxima será de {df_dia["temperature_2m_max"].iloc[0]}°C e a mínima será de {df_dia["temperature_2m_min"].iloc[0]}°C. \n')

#     print(f'A temperatura aparente máxima será de {df_dia["apparent_temperature_max"].iloc[0]}°C e a mínima será de {df_dia["apparent_temperature_min"].iloc[0]}°C. \n')
#     print(f'A velocidade máxima do vento será de {df_dia["wind_speed_10m_max"].iloc[0]} km/h. \n')
#     print(f'O índice UV máximo será de {df_dia["uv_index_max"].iloc[0]}. \n')
#     print('---------------------------------\n')

df = pegar_dados(-23.55, -46.63)

class Metereologia:
     def init__(self,data_frame):
         self.dt = list(data_frame['time'])
         self.datas = list(data_frame['time'])
         self.temp_max = data_frame['temperature_2m_max']
         self.temp_min = data_frame['temperature_2m_min']
         self.temp_aparente_max = data_frame['apparent_temperature_max']
         self.temp_aparente_min = data_frame['apparent_temperature_min']
         self.vento_max = data_frame['wind_speed_10m_max']
         self.indice_uv = data_frame['uv_index_max']
         

     def mostrar_dados(self):
            for self.data in self.datas:
                print(f'Dados do dia: {self.data} \n')
                print(f'No dia {self.data} a temperatura máxima será de {self.temp_max}°C e a mínima será de {self.temp_min}°C. \n')
                print(f'A temperatura aparente máxima será de {self.temp_aparente_max}°C e a mínima será de {self.temp_aparente_min}°C. \n')
                print(f'A velocidade máxima do vento será de {self.vento_max} km/h. \n')
                print(f'O índice UV máximo será de {self.indice_uv}. \n')
                print('---------------------------------\n')


dados_climaticos = Metereologia(
    list(df['time']),
    df['temperature_2m_max'].iloc[0],
    df['temperature_2m_min'].iloc[0],
    df['apparent_temperature_max'].iloc[0],
    df['apparent_temperature_min'].iloc[0],
    df['wind_speed_10m_max'].iloc[0],
    df['uv_index_max'].iloc[0]
)


dados_climaticos.mostrar_dados()