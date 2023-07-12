import requests
import pandas as pd
from pandas import json_normalize
import json
from sqlalchemy import create_engine
from datetime import datetime,date
from datetime import timedelta
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler
from bs4 import BeautifulSoup
from time import sleep
import csv
from scipy import spatial
from sklearn import preprocessing
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np
from statistics import mode
import datetime
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import euclidean_distances

# Leer el archivo Excel
df = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS NORMALIZADOS COMPLETOS CON RENDIMIENTO.xlsx")

# Filtrar el DataFrame 'df' por los valores de 'Level' que sean 1, 2 o 3
df = df[df['Level'].isin([1, 2, 3, 4, 5])]

df['Index'] = df.apply(lambda row: '.'.join([str(row['Full name']), str(row['Team']), str(row['Domestic League']), str(row['Primary position'])]), axis=1)

newcastle_players = df[df['Team'] == 'Newcastle United']
newcastle_names = pd.DataFrame({'Full name': newcastle_players['Full name']})
print(newcastle_names)


# Especifica el nombre del jugador seleccionado
jugador_seleccionado = 'Sergej Milinković-Savić'

# Filtra el DataFrame para obtener los datos del jugador seleccionado
jugador = df[df['Full name'] == jugador_seleccionado]

# Excluye las columnas no deseadas (como 'Index' y otras) y obtén las métricas restantes
player_metrics = jugador.drop(['Index', 'Full name', 'Primary position', 'Age', 'Level', 'Market value', 'Contract expires',
                               "Name", "Team", "Domestic League", "Primary position, %", "On loan", "Birth country", "Birth date", "Foot", "Height", "Weight", "Last club",
                               "Secondary position", "Secondary position, %", "Third position", "Third position, %", "Passport country 1",
                               "Passport country 2", "Games played", "Minutes played", 'Rendimiento porteros juego de pies', 'Grupo porteros juego de pies',
                               'Rendimiento porteros acciones bajo palos', 'Grupo porteros acciones bajo palos', 'Rendimiento porteros dominadores de area',
                               'Grupo porteros dominadores de area', 'Rendimiento centrales salida de balón', 'Grupo centrales salida de balón',
                               'Rendimiento centrales dominadores aéreos', 'Grupo centrales dominadores aéreos','Rendimiento centrales espacios amplios',
                               'Grupo centrales espacios amplios', 'Rendimiento laterales recorridos amplios', 'Grupo laterales recorridos amplios',
                               'Rendimiento laterales asociativos', 'Grupo laterales asociativos', 'Rendimiento laterales posicionales', 'Grupo laterales posicionales',
                               'Rendimiento mediocentros box-to-box', 'Grupo mediocentros box-to-box', 'Rendimiento mediocentros organizativos',
                               'Grupo mediocentros organizativos', 'Rendimiento mediocentros defensivos', 'Grupo mediocentros defensivos',
                               'Rendimiento mediocentros finalizadores', 'Grupo mediocentros finalizadores', 'Rendimiento mediocentros ofensivos asociativos',
                               'Grupo mediocentros ofensivos asociativos', 'Rendimiento mediocentros ofensivos desequilibrantes', 'Grupo mediocentros ofensivos desequilibrantes',
                               'Rendimiento extremos desmarques espacios', 'Grupo extremos desmarques espacios', 'Rendimiento extremos regateadores',
                               'Grupo extremos regateadores', 'Rendimiento extremos asociativos', 'Grupo extremos asociativos', 'Rendimiento delanteros espacios amplios',
                               'Grupo delanteros espacios amplios', 'Rendimiento delanteros asociativos', 'Grupo delanteros asociativos',
                               'Rendimiento delanteros referencia', 'Grupo delanteros referencia', 'Successful back passes, %', 'Average long pass lenght', 'Average pass lenght',
                               'Accurate short medium passes, %', 'Back passes per 90', 'Back passes to gk per 90', 'Penalties conversion, %', 'Yellow cards'], axis=1)

# para eliminar otras metricas que no interesen agregarlas abajo
# player_metrics = jugador.drop([''], axis=1)

# Encuentra las 8 métricas en las que el jugador seleccionado destaca más
destaques_indices = np.argsort(player_metrics.values[0])[::-1][:8]
destaques_nombres = player_metrics.columns[destaques_indices]
destaques_valores = player_metrics.values[0, destaques_indices]

# Crea un nuevo DataFrame con las métricas destacadas y sus valores
destaques = pd.DataFrame({metrica: [valor] for metrica, valor in zip(destaques_nombres, destaques_valores)})

# Agrega las columnas del DataFrame original al DataFrame destaques
destaques = pd.concat([jugador[['Full name', 'Primary position', 'Age', 'Level', 'Team', 'Domestic League', 'Market value', 'Contract expires', 'Index']], destaques], axis=1)

# Imprime el DataFrame final
print(destaques)

# Obtener las métricas destacadas del jugador seleccionado
metricas_destacadas = destaques_nombres.tolist()

# Filtrar el DataFrame original para obtener los jugadores con valores similares en las métricas destacadas
jugadores_similares = df[df.apply(lambda row: np.all(row[metricas_destacadas] == destaques_valores), axis=1)]

# Calculamos las distancias euclidianas entre el jugador seleccionado y todos los demás jugadores
distancias = euclidean_distances(jugador[destaques_nombres].values, df[destaques_nombres].values)
distancias = distancias.reshape(-1)

# Agregamos la columna "coeficiente similitud" al DataFrame original
df['Coeficiente similitud'] = distancias

# Filtramos y seleccionamos los 50 jugadores más similares
jugadores_similares = df.nsmallest(1551, 'Coeficiente similitud')[1:]

# Mostramos los 50 jugadores más similares
print(jugadores_similares)

# Añadir una columna "Coeficiente similitud" al DataFrame destaques con valor 0 para el jugador seleccionado
destaques['Coeficiente similitud'] = 0

# Concatenar los DataFrames destaques y jugadores_similares
resultado_final = pd.concat([destaques, jugadores_similares])

# Ordenar los jugadores por coeficiente de similitud de forma ascendente
resultado_final = resultado_final.sort_values('Coeficiente similitud')

# Mostrar el resultado final
print(resultado_final)

# resultado_final_filtrado = resultado_final[(resultado_final['Primary position'].isin(['LB', 'LWB'])) & (resultado_final['Age'] < 30) & (resultado_final['Minutes played'] > 1500)]

resultado_final_filtrado = resultado_final[(resultado_final['Primary position'].isin(['RCMF', 'LCMF', 'LDMF', 'RDMF', 'DMF'])) & (resultado_final['Age'] < 30)]
