import pandas as pd

dados = {
    "capital": [
        "Rio Branco", "Maceió", "Macapá", "Manaus", "Salvador",
        "Fortaleza", "Brasília", "Vitória", "Goiânia", "São Luís",
        "Cuiabá", "Campo Grande", "Belo Horizonte", "Belém",
        "João Pessoa", "Curitiba", "Recife", "Teresina", "Rio de Janeiro",
        "Natal", "Porto Alegre", "Porto Velho", "Boa Vista",
        "Florianópolis", "Aracaju", "São Paulo", "Palmas"
    ],
    "estado": [
        "AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA",
        "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN",
        "RS", "RO", "RR", "SC", "SE", "SP", "TO"
    ],
    "latitude": [
        -9.97, -9.67, 0.03, -3.10, -12.97,
        -3.73, -15.79, -20.32, -16.68, -2.53,
        -15.60, -20.44, -19.92, -1.46, -7.12,
        -25.43, -8.05, -5.09, -22.91, -5.80,
        -30.03, -8.76, 2.82, -27.60, -10.92,
        -23.55, -10.18
    ],
    "longitude": [
        -67.82, -35.74, -51.05, -60.03, -38.51,
        -38.53, -47.88, -40.34, -49.25, -44.30,
        -56.10, -54.65, -43.93, -48.50, -34.86,
        -49.27, -34.90, -42.80, -43.20, -35.21,
        -51.23, -63.90, -60.67, -48.55, -37.08,
        -46.63, -48.33
    ]
}

df_capitais = pd.DataFrame(dados)


