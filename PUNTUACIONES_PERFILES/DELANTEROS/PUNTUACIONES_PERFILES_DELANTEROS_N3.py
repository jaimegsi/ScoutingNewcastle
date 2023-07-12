import pandas as pd
import openpyxl
import numpy as np

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL3 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 700]
print(n1)

#Separar los frames por posiciones y perfiles
df_dc = n1[n1['Primary position'] == 'CF'].copy()
df_dc_aso = n1[n1['Primary position'] == 'CF'].copy()
df_dc_esp = n1[n1['Primary position'] == 'CF'].copy()
df_dc_ref = n1[n1['Primary position'] == 'CF'].copy()

# DELANTEROS (ASOCIATIVOS)

def calcular_rendimiento(df_dc_aso, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_dc_aso[metricas_seleccionadas].mean()
    stds = df_dc_aso[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dc_aso_norm = (df_dc_aso[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_dc_aso[metrica + '_puntuacion'] = df_dc_aso_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dc_aso['puntuacion_total'] = df_dc_aso[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_dc_aso['puntuacion_total'].max()
    puntuacion_minima = df_dc_aso['puntuacion_total'].min()

    df_dc_aso['Rendimiento delanteros asociativos'] = ((df_dc_aso['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    percentiles = np.percentile(df_dc_aso['Rendimiento delanteros asociativos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_dc_aso['Rendimiento delanteros asociativos']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_dc_aso['Grupo delanteros asociativos'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_dc_aso[metrica + '_puntuacion_norm'] = df_dc_aso_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento delanteros asociativos',
                                                 'Grupo delanteros asociativos']

    # Reorganizar las columnas del DataFrame
    df_dc_aso = df_dc_aso.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dc_aso = df_dc_aso.round(2)

    # Ordenar el DataFrame df_dc_aso de mayor a menor según la columna 'Rendimiento'
    df_dc_aso = df_dc_aso.sort_values(by='Rendimiento delanteros asociativos', ascending=False)

    return df_dc_aso

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Differential xG / Goals per 90', 'Shot assists per 90', 'Touches in the box per 90', 'Key passes per 90', 'xA per 90', 'Successful passes to penalty area per 90 (number)', 'Successful attacking actions per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.1, 0.5, 0.25, 0.5, 0.1, 0.25, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Differential xG / Goals per 90', 'Shot assists per 90', 'Touches in the box per 90', 'Key passes per 90', 'xA per 90', 'Successful passes to penalty area per 90 (number)', 'Successful attacking actions per 90']

# Llama a la función calcular_rendimiento
resultado_dc_aso = calcular_rendimiento(df_dc_aso, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_dc_aso)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# DELANTEROS (ESPACIOS)

def calcular_rendimiento1(df_dc_esp, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_dc_esp[metricas_seleccionadas1].mean()
    stds1 = df_dc_esp[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dc_esp_norm = (df_dc_esp[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_dc_esp[metrica1 + '_puntuacion'] = df_dc_esp_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dc_esp['puntuacion_total'] = df_dc_esp[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_dc_esp['puntuacion_total'].max()
    puntuacion_minima1 = df_dc_esp['puntuacion_total'].min()

    df_dc_esp['Rendimiento delanteros espacios amplios'] = ((df_dc_esp['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_dc_esp['Rendimiento delanteros espacios amplios'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_dc_esp['Rendimiento delanteros espacios amplios']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_dc_esp['Grupo delanteros espacios amplios'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_dc_esp[metrica1 + '_puntuacion_norm'] = df_dc_esp_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento delanteros espacios amplios',
                                                 'Grupo delanteros espacios amplios']

    # Reorganizar las columnas del DataFrame
    df_dc_esp = df_dc_esp.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dc_esp = df_dc_esp.round(2)

    # Ordenar el DataFrame df_dc_esp de mayor a menor según la columna 'Rendimiento'
    df_dc_esp = df_dc_esp.sort_values(by='Rendimiento delanteros espacios amplios', ascending=False)

    return df_dc_esp

# Resto del código
metricas_seleccionadas1 = ['Successful attacking actions per 90', 'Accelerations per 90', 'Received passes per 90', 'Received long passes per 90', 'Successful dribbles per 90 (number)', 'Progressive runs per 90', 'Differential xG / Goals per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.1, 0.25, 0.1, 0.5, 0.1, 0.25, 0.25]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful attacking actions per 90', 'Accelerations per 90', 'Received passes per 90', 'Received long passes per 90', 'Successful dribbles per 90 (number)', 'Progressive runs per 90', 'Differential xG / Goals per 90']

# Llama a la función calcular_rendimiento1 con df_dc_esp
resultado_dc_esp = calcular_rendimiento1(df_dc_esp, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_dc_esp
print(resultado_dc_esp)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# DELANTERO (REFERENCIA)

def calcular_rendimiento2(df_dc_ref, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_dc_ref[metricas_seleccionadas2].mean()
    stds2 = df_dc_ref[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dc_ref_norm = (df_dc_ref[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_dc_ref[metrica2 + '_puntuacion'] = df_dc_ref_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dc_ref['puntuacion_total'] = df_dc_ref[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_dc_ref['puntuacion_total'].max()
    puntuacion_minima2 = df_dc_ref['puntuacion_total'].min()

    df_dc_ref['Rendimiento delanteros referencia'] = ((df_dc_ref['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_dc_ref['Rendimiento delanteros referencia'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_dc_ref['Rendimiento delanteros referencia']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_dc_ref['Grupo delanteros referencia'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_dc_ref[metrica2 + '_puntuacion_norm'] = df_dc_ref_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento delanteros referencia',
                                                 'Grupo delanteros referencia']

    # Reorganizar las columnas del DataFrame
    df_dc_ref = df_dc_ref.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dc_ref = df_dc_ref.round(2)

    # Ordenar el DataFrame df_dc_ref de mayor a menor según la columna 'Rendimiento'
    df_dc_ref = df_dc_ref.sort_values(by='Rendimiento delanteros referencia', ascending=False)

    return df_dc_ref

# Resto del código
metricas_seleccionadas2 = ['Shots on target, %', 'Goals', 'Goals per 90', 'Received passes per 90', 'Successful attacking actions per 90', 'Won aerial duels per 90 (number)', 'Differential xG / Goals per 90', 'Head goals per 90', 'Head goals', 'Touches in the box per 90']
pesos2 = [0.25, 0.1, 0.5, 0.25, 0.1, 0.5, 0.5, 0.25, 0.1, 0.1]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Shots on target, %', 'Goals', 'Goals per 90', 'Received passes per 90', 'Successful attacking actions per 90', 'Won aerial duels per 90 (number)', 'Differential xG / Goals per 90', 'Head goals per 90', 'Head goals', 'Touches in the box per 90']

resultado_dc_ref = calcular_rendimiento2(df_dc_ref, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_dc_ref)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_dc, resultado_dc_esp, resultado_dc_aso, resultado_dc_ref]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_dc_completo = df_dc.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_dc_completo.columns]
    df_dc_completo = pd.concat([df_dc_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_dc_completo.to_excel('df_dc_n3.xlsx', index=True)






