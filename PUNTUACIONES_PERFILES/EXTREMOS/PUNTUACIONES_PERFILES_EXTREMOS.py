import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL1 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 700]
print(n1)


#Separar los frames por posiciones y perfiles
df_ex = n1[n1['Primary position'].isin(['LW', 'LWF', 'LAMF', 'RW', 'RWF', 'RAMF'])].copy()
df_ex_aso = n1[n1['Primary position'].isin(['LW', 'LWF', 'LAMF', 'RW', 'RWF', 'RAMF'])].copy()
df_ex_reg = n1[n1['Primary position'].isin(['LW', 'LWF', 'LAMF', 'RW', 'RWF', 'RAMF'])].copy()
df_ex_des = n1[n1['Primary position'].isin(['LW', 'LWF', 'LAMF', 'RW', 'RWF', 'RAMF'])].copy()

# EXTREMOS (ASOCIATIVOS)

import pandas as pd
import numpy as np

def calcular_rendimiento(df_ex_aso, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_ex_aso[metricas_seleccionadas].mean()
    stds = df_ex_aso[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_ex_aso_norm = (df_ex_aso[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_ex_aso[metrica + '_puntuacion'] = df_ex_aso_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_ex_aso['puntuacion_total'] = df_ex_aso[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_ex_aso['puntuacion_total'].max()
    puntuacion_minima = df_ex_aso['puntuacion_total'].min()

    df_ex_aso['Rendimiento extremos asociativos'] = ((df_ex_aso['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    percentiles = np.percentile(df_ex_aso['Rendimiento extremos asociativos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_ex_aso['Rendimiento extremos asociativos']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_ex_aso['Grupo extremos asociativos'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_ex_aso[metrica + '_puntuacion_norm'] = df_ex_aso_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento extremos asociativos',
                                                 'Grupo extremos asociativos']

    # Reorganizar las columnas del DataFrame
    df_ex_aso = df_ex_aso.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_ex_aso = df_ex_aso.round(2)

    # Ordenar el DataFrame df_ex_aso de mayor a menor según la columna 'Rendimiento'
    df_ex_aso = df_ex_aso.sort_values(by='Rendimiento extremos asociativos', ascending=False)

    return df_ex_aso

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Key passes per 90', 'xA per 90', 'Successful passes to penalty area per 90 (number)', 'Successful smart passes per 90 (number)', 'Cross to goalie box per 90', 'Successful attacking actions per 90', 'Successful crosses per 90 (number)']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.5, 0.5, 0.25, 0.25, 0.1, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Key passes per 90', 'xA per 90', 'Successful passes to penalty area per 90 (number)', 'Successful smart passes per 90 (number)', 'Cross to goalie box per 90', 'Successful attacking actions per 90', 'Successful crosses per 90 (number)']

# Llama a la función calcular_rendimiento
resultado_ex_aso = calcular_rendimiento(df_ex_aso, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_ex_aso)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# EXTREMOS (REGATE)

def calcular_rendimiento1(df_ex_reg, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_ex_reg[metricas_seleccionadas1].mean()
    stds1 = df_ex_reg[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_ex_reg_norm = (df_ex_reg[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_ex_reg[metrica1 + '_puntuacion'] = df_ex_reg_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_ex_reg['puntuacion_total'] = df_ex_reg[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_ex_reg['puntuacion_total'].max()
    puntuacion_minima1 = df_ex_reg['puntuacion_total'].min()

    df_ex_reg['Rendimiento extremos regateadores'] = ((df_ex_reg['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_ex_reg['Rendimiento extremos regateadores'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_ex_reg['Rendimiento extremos regateadores']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_ex_reg['Grupo extremos regateadores'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_ex_reg[metrica1 + '_puntuacion_norm'] = df_ex_reg_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento extremos regateadores',
                                                 'Grupo extremos regateadores']

    # Reorganizar las columnas del DataFrame
    df_ex_reg = df_ex_reg.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_ex_reg = df_ex_reg.round(2)

    # Ordenar el DataFrame df_ex_reg de mayor a menor según la columna 'Rendimiento'
    df_ex_reg = df_ex_reg.sort_values(by='Rendimiento extremos regateadores', ascending=False)

    return df_ex_reg

# Resto del código
metricas_seleccionadas1 = ['Successful dribbles per 90 (number)', 'Dribbles per 90', 'Progressive runs per 90', 'Accelerations per 90', 'Differential xG / Goals per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.5, 0.25, 0.5, 0.1, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful dribbles per 90 (number)', 'Dribbles per 90', 'Progressive runs per 90', 'Accelerations per 90', 'Differential xG / Goals per 90']

# Llama a la función calcular_rendimiento1 con df_ex_reg
resultado_ex_reg = calcular_rendimiento1(df_ex_reg, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_ex_reg
print(resultado_ex_reg)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# EXTREMOS (DESMARQUE ESPACIOS)

def calcular_rendimiento2(df_ex_des, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_ex_des[metricas_seleccionadas2].mean()
    stds2 = df_ex_des[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_ex_des_norm = (df_ex_des[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_ex_des[metrica2 + '_puntuacion'] = df_ex_des_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_ex_des['puntuacion_total'] = df_ex_des[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_ex_des['puntuacion_total'].max()
    puntuacion_minima2 = df_ex_des['puntuacion_total'].min()

    df_ex_des['Rendimiento extremos desmarques espacios'] = ((df_ex_des['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_ex_des['Rendimiento extremos desmarques espacios'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_ex_des['Rendimiento extremos desmarques espacios']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_ex_des['Grupo extremos desmarques espacios'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_ex_des[metrica2 + '_puntuacion_norm'] = df_ex_des_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento extremos desmarques espacios',
                                                 'Grupo extremos desmarques espacios']

    # Reorganizar las columnas del DataFrame
    df_ex_des = df_ex_des.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_ex_des = df_ex_des.round(2)

    # Ordenar el DataFrame df_ex_des de mayor a menor según la columna 'Rendimiento'
    df_ex_des = df_ex_des.sort_values(by='Rendimiento extremos desmarques espacios', ascending=False)

    return df_ex_des

# Resto del código
metricas_seleccionadas2 = ['xA per 90', 'Assists per 90', 'Accelerations per 90', 'Received passes per 90', 'Received long passes per 90', 'Successful attacking actions per 90', 'Progressive runs per 90']
pesos2 = [0.1, 0.25, 0.1, 0.25, 0.5, 0.25, 0.25]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'xA per 90', 'Assists per 90', 'Accelerations per 90', 'Received passes per 90', 'Received long passes per 90', 'Successful attacking actions per 90', 'Progressive runs per 90']

resultado_ex_des = calcular_rendimiento2(df_ex_des, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_ex_des)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_ex, resultado_ex_des, resultado_ex_reg, resultado_ex_aso]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_ex_completo = df_ex.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_ex_completo.columns]
    df_ex_completo = pd.concat([df_ex_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_ex_completo.to_excel('df_ex_n1.xlsx', index=True)






