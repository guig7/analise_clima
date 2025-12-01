class Metereologia:
     def __init__(self, datas, temp_maxs, temp_mins, temp_aparente_maxs, temp_aparente_mins, vento_maxs, indice_uvs):
         self.datas = datas
         self.temp_maxs = temp_maxs
         self.temp_mins = temp_mins
         self.temp_aparente_maxs = temp_aparente_maxs
         self.temp_aparente_mins = temp_aparente_mins
         self.vento_maxs = vento_maxs
         self.indice_uvs = indice_uvs

     def mostrar_dados(self):
            for x in range(len(self.datas)):
                print(f'Dados do dia: {self.datas[x]} \n')
                print(f'No dia {self.datas[x]} a temperatura máxima será de {self.temp_maxs[x]}°C e a mínima será de {self.temp_mins[x]}°C. \n')
                print(f'A temperatura aparente máxima será de {self.temp_aparente_maxs[x]}°C e a mínima será de {self.temp_aparente_mins[x]}°C. \n')
                print(f'A velocidade máxima do vento será de {self.vento_maxs[x]} km/h. \n')
                print(f'O índice UV máximo será de {self.indice_uvs[x]}. \n')
                print('---------------------------------\n')


