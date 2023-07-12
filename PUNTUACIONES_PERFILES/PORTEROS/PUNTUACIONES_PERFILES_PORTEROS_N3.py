import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL3 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 1200]
print(n1)


#Separar los frames por posiciones y perfiles
df_por = n1[n1['Primary position'] == 'GK'].copy()
df_por_are = n1[n1['Primary position'] == 'GK'].copy()
df_por_pal = n1[n1['Primary position'] == 'GK'].copy()
df_por_pie = n1[n1['Primary position'] == 'GK'].copy()

# PORTERO (DOMINADOR AREA)
print(df_por_are)

def calcular_rendimiento(df_por_are, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_por_are[metricas_seleccionadas].mean()
    stds = df_por_are[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_por_are_norm = (df_por_are[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_por_are[metrica + '_puntuacion'] = df_por_are_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_por_are['puntuacion_total'] = df_por_are[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_por_are['puntuacion_total'].max()
    puntuacion_minima = df_por_are['puntuacion_total'].min()

    df_por_are['Rendimiento porteros dominadores de area'] = ((df_por_are['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles = np.percentile(df_por_are['Rendimiento porteros dominadores de area'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_por_are['Rendimiento porteros dominadores de area']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_por_are['Grupo porteros dominadores de area'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_por_are[metrica + '_puntuacion_norm'] = df_por_are_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento porteros dominadores de area',
                                                 'Grupo porteros dominadores de area']

    # Reorganizar las columnas del DataFrame
    df_por_are = df_por_are.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_por_are = df_por_are.round(2)

    # Ordenar el DataFrame df_por_are de mayor a menor según la columna 'Rendimiento'
    df_por_are = df_por_are.sort_values(by='Rendimiento porteros dominadores de area', ascending=False)

    return df_por_are

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Aerial duels won, %', 'Won aerial duels per 90 (number)', 'Goalkeeper exits per 90', 'Gk aerial duels per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.25, 0.25, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Aerial duels won, %', 'Won aerial duels per 90 (number)', 'Goalkeeper exits per 90', 'Gk aerial duels per 90']

# Llama a la función calcular_rendimiento
resultado_por_are = calcular_rendimiento(df_por_are, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_por_are)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# PORTERO (ACCIONES BAJO PALOS)

def calcular_rendimiento1(df_por_pal, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_por_pal[metricas_seleccionadas1].mean()
    stds1 = df_por_pal[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_por_pal_norm = (df_por_pal[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_por_pal[metrica1 + '_puntuacion'] = df_por_pal_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_por_pal['puntuacion_total'] = df_por_pal[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_por_pal['puntuacion_total'].max()
    puntuacion_minima1 = df_por_pal['puntuacion_total'].min()

    df_por_pal['Rendimiento porteros acciones bajo palos'] = ((df_por_pal['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_por_pal['Rendimiento porteros acciones bajo palos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_por_pal['Rendimiento porteros acciones bajo palos']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_por_pal['Grupo porteros acciones bajo palos'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_por_pal[metrica1 + '_puntuacion_norm'] = df_por_pal_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento porteros acciones bajo palos',
                                                 'Grupo porteros acciones bajo palos']

    # Reorganizar las columnas del DataFrame
    df_por_pal = df_por_pal.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_por_pal = df_por_pal.round(2)

    # Ordenar el DataFrame df_por_are de mayor a menor según la columna 'Rendimiento'
    df_por_pal = df_por_pal.sort_values(by='Rendimiento porteros acciones bajo palos', ascending=False)

    return df_por_pal

# Resto del código
metricas_seleccionadas1 = ['Prevented goals per 90', 'Differential xG / Goals against per 90', 'Saves, %', 'Shots per gol against']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.5, 0.5, 0.25, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Prevented goals per 90', 'Differential xG / Goals against per 90', 'Saves, %', 'Shots per gol against']

# Llama a la función calcular_rendimiento con df_por_are
resultado_por_pal = calcular_rendimiento1(df_por_pal, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_por_are1
print(resultado_por_pal)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# PORTERO (JUEGO DE PIES)
def calcular_rendimiento2(df_por_pie, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_por_pie[metricas_seleccionadas2].mean()
    stds2 = df_por_pie[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_por_pie_norm = (df_por_pie[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_por_pie[metrica2 + '_puntuacion'] = df_por_pie_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_por_pie['puntuacion_total'] = df_por_pie[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_por_pie['puntuacion_total'].max()
    puntuacion_minima2 = df_por_pie['puntuacion_total'].min()

    df_por_pie['Rendimiento porteros juego de pies'] = ((df_por_pie['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_por_pie['Rendimiento porteros juego de pies'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_por_pie['Rendimiento porteros juego de pies']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_por_pie['Grupo porteros juego de pies'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_por_pie[metrica2 + '_puntuacion_norm'] = df_por_pie_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento porteros juego de pies',
                                                 'Grupo porteros juego de pies']

    # Reorganizar las columnas del DataFrame
    df_por_pie = df_por_pie.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_por_pie = df_por_pie.round(2)

    # Ordenar el DataFrame df_por_pal2 de mayor a menor según la columna 'Rendimiento'
    df_por_pie = df_por_pie.sort_values(by='Rendimiento porteros juego de pies', ascending=False)

    return df_por_pie

# Resto del código
metricas_seleccionadas2 = ['Successful long passes, %', 'Accurate passes to final third, %', 'Successful progressive passes, %']
pesos2 = [0.5, 0.25, 0.1]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful long passes, %', 'Accurate passes to final third, %', 'Successful progressive passes, %']

resultado_por_pie = calcular_rendimiento2(df_por_pie, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_por_pie)


# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_por, resultado_por_pie, resultado_por_pal, resultado_por_are]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_por_completo = df_por.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_por_completo.columns]
    df_por_completo = pd.concat([df_por_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_por_completo.to_excel('df_por_n3.xlsx', index=True)






