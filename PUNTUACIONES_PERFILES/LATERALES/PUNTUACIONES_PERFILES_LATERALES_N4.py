import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL4 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 700]
print(n1)


#Separar los frames por posiciones y perfiles
df_lat = n1[n1['Primary position'].isin(['RB', 'RWB', 'LB', 'LWB'])].copy()
df_lat_rec = n1[n1['Primary position'].isin(['RB', 'RWB', 'LB', 'LWB'])].copy()
df_lat_aso = n1[n1['Primary position'].isin(['RB', 'RWB', 'LB', 'LWB'])].copy()
df_lat_pos = n1[n1['Primary position'].isin(['RB', 'RWB', 'LB', 'LWB'])].copy()


df_ltd = n1[n1['Primary position'].isin(['RB', 'RWB'])].copy()
df_ltd_rec = n1[n1['Primary position'].isin(['RB', 'RWB'])].copy()
df_ltd_aso = n1[n1['Primary position'].isin(['RB', 'RWB'])].copy()
df_ltd_pos = n1[n1['Primary position'].isin(['RB', 'RWB'])].copy()
df_lti = n1[n1['Primary position'].isin(['LB', 'LWB'])].copy()
df_lti_rec = n1[n1['Primary position'].isin(['LB', 'LWB'])].copy()
df_lti_aso = n1[n1['Primary position'].isin(['LB', 'LWB'])].copy()
df_lti_pos = n1[n1['Primary position'].isin(['LB', 'LWB'])].copy()

# LATERALES RECORRIDO AMPLIO

def calcular_rendimiento(df_lat_rec, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_lat_rec[metricas_seleccionadas].mean()
    stds = df_lat_rec[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_lat_rec_norm = (df_lat_rec[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_lat_rec[metrica + '_puntuacion'] = df_lat_rec_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_lat_rec['puntuacion_total'] = df_lat_rec[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_lat_rec['puntuacion_total'].max()
    puntuacion_minima = df_lat_rec['puntuacion_total'].min()

    df_lat_rec['Rendimiento laterales recorridos amplios'] = ((df_lat_rec['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles = np.percentile(df_lat_rec['Rendimiento laterales recorridos amplios'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_lat_rec['Rendimiento laterales recorridos amplios']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_lat_rec['Grupo laterales recorridos amplios'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_lat_rec[metrica + '_puntuacion_norm'] = df_lat_rec_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento laterales recorridos amplios',
                                                 'Grupo laterales recorridos amplios']

    # Reorganizar las columnas del DataFrame
    df_lat_rec = df_lat_rec.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_lat_rec = df_lat_rec.round(2)

    # Ordenar el DataFrame df_lat_rec de mayor a menor según la columna 'Rendimiento'
    df_lat_rec = df_lat_rec.sort_values(by='Rendimiento laterales recorridos amplios', ascending=False)

    return df_lat_rec

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Accelerations per 90', 'Progressive runs per 90', 'Accurate crosses, %', 'Accurate passes to penalty area, %', 'Successful defensive actions per 90', 'Won defensive duels per 90 (number)', 'Aerial duels won, %', 'Successful progressive passes per 90 (number)', 'Won offensive duels per 90 (number)']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.5, 0.5, 0.25, 0.25, 0.25, 0.1, 0.25, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Accelerations per 90', 'Progressive runs per 90', 'Accurate crosses, %', 'Accurate passes to penalty area, %', 'Successful defensive actions per 90', 'Won defensive duels per 90 (number)', 'Aerial duels won, %', 'Successful progressive passes per 90 (number)', 'Won offensive duels per 90 (number)']

# Llama a la función calcular_rendimiento
resultado_lat_rec = calcular_rendimiento(df_lat_rec, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_lat_rec)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# LATERALES ASOCIATIVOS

def calcular_rendimiento1(df_lat_aso, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_lat_aso[metricas_seleccionadas1].mean()
    stds1 = df_lat_aso[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_lat_aso_norm = (df_lat_aso[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_lat_aso[metrica1 + '_puntuacion'] = df_lat_aso_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_lat_aso['puntuacion_total'] = df_lat_aso[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_lat_aso['puntuacion_total'].max()
    puntuacion_minima1 = df_lat_aso['puntuacion_total'].min()

    df_lat_aso['Rendimiento laterales asociativos'] = ((df_lat_aso['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_lat_aso['Rendimiento laterales asociativos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_lat_aso['Rendimiento laterales asociativos']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_lat_aso['Grupo laterales asociativos'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_lat_aso[metrica1 + '_puntuacion_norm'] = df_lat_aso_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento laterales asociativos',
                                                 'Grupo laterales asociativos']

    # Reorganizar las columnas del DataFrame
    df_lat_aso = df_lat_aso.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_lat_aso = df_lat_aso.round(2)

    # Ordenar el DataFrame df_lat_aso de mayor a menor según la columna 'Rendimiento'
    df_lat_aso = df_lat_aso.sort_values(by='Rendimiento laterales asociativos', ascending=False)

    return df_lat_aso

# Resto del código
metricas_seleccionadas1 = [ 'Deep completed crosses per 90','Won defensive duels per 90 (number)', 'Won aerial duels per 90 (number)', 'Successful crosses per 90 (number)', 'Successful passes per 90 (number)', 'Successful passes to final third per 90 (number)', 'Successful progressive passes per 90 (number)', 'Successful long passes per 90 (number)']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.1, 0.25, 0.25, 0.5, 0.5, 0.5, 0.25, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Won defensive duels per 90 (number)', 'Aerial duels won, %', 'Successful crosses per 90 (number)', 'Successful passes per 90 (number)', 'Forward successful passes per 90 (number)', 'Successful passes to final third per 90 (number)', 'Successful progressive passes per 90 (number)', 'Successful long passes per 90 (number)']

# Llama a la función calcular_rendimiento1 con df_lat_aso
resultado_lat_aso = calcular_rendimiento1(df_lat_aso, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_lat_aso
print(resultado_lat_aso)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# LATERALES POSICIONALES
def calcular_rendimiento2(df_lat_pos, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_lat_pos[metricas_seleccionadas2].mean()
    stds2 = df_lat_pos[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_lat_pos_norm = (df_lat_pos[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_lat_pos[metrica2 + '_puntuacion'] = df_lat_pos_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_lat_pos['puntuacion_total'] = df_lat_pos[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_lat_pos['puntuacion_total'].max()
    puntuacion_minima2 = df_lat_pos['puntuacion_total'].min()

    df_lat_pos['Rendimiento laterales posicionales'] = ((df_lat_pos['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_lat_pos['Rendimiento laterales posicionales'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_lat_pos['Rendimiento laterales posicionales']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_lat_pos['Grupo laterales posicionales'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_lat_pos[metrica2 + '_puntuacion_norm'] = df_lat_pos_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento laterales posicionales',
                                                 'Grupo laterales posicionales']

    # Reorganizar las columnas del DataFrame
    df_lat_pos = df_lat_pos.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_lat_pos = df_lat_pos.round(2)

    # Ordenar el DataFrame df_lat_pos de mayor a menor según la columna 'Rendimiento'
    df_lat_pos = df_lat_pos.sort_values(by='Rendimiento laterales posicionales', ascending=False)

    return df_lat_pos

# Resto del código

metricas_seleccionadas2 = ['Successful defensive actions per 90', 'Won duels per 90 (number)', 'Accelerations per 90', 'Successful progressive passes per 90 (number)', 'Won defensive duels per 90 (number)', 'Interceptions per 90', 'Won aerial duels per 90 (number)']
pesos2 = [0.5, 0.5, 0.1, 0.1, 0.25, 0.25, 0.25]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful defensive actions per 90', 'Won duels per 90 (number)', 'Accelerations per 90', 'Successful progressive passes per 90 (number)', 'Won defensive duels per 90 (number)', 'Interceptions per 90', 'Won aerial duels per 90 (number)']

resultado_lat_pos = calcular_rendimiento2(df_lat_pos, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_lat_pos)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_lat, resultado_lat_rec, resultado_lat_aso, resultado_lat_pos]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_lat_completo = df_lat.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_lat_completo.columns]
    df_lat_completo = pd.concat([df_lat_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_lat_completo.to_excel('df_lat_n4.xlsx', index=True)






