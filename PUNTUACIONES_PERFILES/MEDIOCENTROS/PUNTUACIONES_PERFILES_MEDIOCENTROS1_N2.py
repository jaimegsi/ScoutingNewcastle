import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL2 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 700]
print(n1)


#Separar los frames por posiciones y perfiles
df_mc = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_def = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_org = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_box = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_aso= n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_des = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()
df_mc_fin = n1[n1['Primary position'].isin(['DMF', 'LDMF', 'RDMF', 'AMF', 'LCMF', 'RCMF'])].copy()

# MEDIOCENTROS (DEFENSIVO)
print(df_mc_def)

def calcular_rendimiento(df_mc_def, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_mc_def[metricas_seleccionadas].mean()
    stds = df_mc_def[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_def_norm = (df_mc_def[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_mc_def[metrica + '_puntuacion'] = df_mc_def_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_def['puntuacion_total'] = df_mc_def[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_mc_def['puntuacion_total'].max()
    puntuacion_minima = df_mc_def['puntuacion_total'].min()

    df_mc_def['Rendimiento mediocentros defensivos'] = ((df_mc_def['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles = np.percentile(df_mc_def['Rendimiento mediocentros defensivos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_mc_def['Rendimiento mediocentros defensivos']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_mc_def['Grupo mediocentros defensivos'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_mc_def[metrica + '_puntuacion_norm'] = df_mc_def_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento mediocentros defensivos',
                                                 'Grupo mediocentros defensivos']

    # Reorganizar las columnas del DataFrame
    df_mc_def = df_mc_def.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_def = df_mc_def.round(2)

    # Ordenar el DataFrame df_mc_def de mayor a menor según la columna 'Rendimiento'
    df_mc_def = df_mc_def.sort_values(by='Rendimiento mediocentros defensivos', ascending=False)

    return df_mc_def

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Successful defensive actions per 90', 'Won defensive duels per 90 (number)', 'Won offensive duels per 90 (number)', 'Won aerial duels per 90 (number)', 'Received passes per 90', 'Successful passes per 90 (number)', 'Interceptions per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.5, 0.25, 0.25, 0.1, 0.1, 0.25]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful defensive actions per 90', 'Won defensive duels per 90 (number)', 'Won offensive duels per 90 (number)', 'Won aerial duels per 90 (number)', 'Received passes per 90', 'Successful passes per 90 (number)', 'Interceptions per 90']

# Llama a la función calcular_rendimiento
resultado_mc_def = calcular_rendimiento(df_mc_def, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_mc_def)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# MEDIOCENTROS (ORGANIZATIVO)

def calcular_rendimiento1(df_mc_org, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_mc_org[metricas_seleccionadas1].mean()
    stds1 = df_mc_org[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_org_norm = (df_mc_org[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_mc_org[metrica1 + '_puntuacion'] = df_mc_org_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_org['puntuacion_total'] = df_mc_org[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_mc_org['puntuacion_total'].max()
    puntuacion_minima1 = df_mc_org['puntuacion_total'].min()

    df_mc_org['Rendimiento mediocentros organizativos'] = ((df_mc_org['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_mc_org['Rendimiento mediocentros organizativos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_mc_org['Rendimiento mediocentros organizativos']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_mc_org['Grupo mediocentros organizativos'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_mc_org[metrica1 + '_puntuacion_norm'] = df_mc_org_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento mediocentros organizativos',
                                                 'Grupo mediocentros organizativos']

    # Reorganizar las columnas del DataFrame
    df_mc_org = df_mc_org.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_org = df_mc_org.round(2)

    # Ordenar el DataFrame df_mc_org de mayor a menor según la columna 'Rendimiento'
    df_mc_org = df_mc_org.sort_values(by='Rendimiento mediocentros organizativos', ascending=False)

    return df_mc_org

# Resto del código
metricas_seleccionadas1 = ['Forward passes per 90', 'Smart passes per 90', 'Successful passes to final third per 90 (number)', 'Received passes per 90', 'Successful long passes per 90 (number)', 'Second assists per 90', 'Third assists per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.5, 0.5, 0.25, 0.25, 0.25, 0.1, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Forward passes per 90', 'Smart passes per 90', 'Successful passes to final third per 90 (number)', 'Received passes per 90', 'Successful long passes per 90 (number)', 'Second assists per 90', 'Third assists per 90']

# Llama a la función calcular_rendimiento1 con df_mc_org
resultado_mc_org = calcular_rendimiento1(df_mc_org, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_mc_org
print(resultado_mc_org)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# MEDIOCENTROS (BOX-TO-BOX)

def calcular_rendimiento2(df_mc_box, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_mc_box[metricas_seleccionadas2].mean()
    stds2 = df_mc_box[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_box_norm = (df_mc_box[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_mc_box[metrica2 + '_puntuacion'] = df_mc_box_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_box['puntuacion_total'] = df_mc_box[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_mc_box['puntuacion_total'].max()
    puntuacion_minima2 = df_mc_box['puntuacion_total'].min()

    df_mc_box['Rendimiento mediocentros box-to-box'] = ((df_mc_box['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_mc_box['Rendimiento mediocentros box-to-box'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_mc_box['Rendimiento mediocentros box-to-box']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_mc_box['Grupo mediocentros box-to-box'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_mc_box[metrica2 + '_puntuacion_norm'] = df_mc_box_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento mediocentros box-to-box',
                                                 'Grupo mediocentros box-to-box']

    # Reorganizar las columnas del DataFrame
    df_mc_box = df_mc_box.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_box = df_mc_box.round(2)

    # Ordenar el DataFrame df_mc_box de mayor a menor según la columna 'Rendimiento'
    df_mc_box = df_mc_box.sort_values(by='Rendimiento mediocentros box-to-box', ascending=False)

    return df_mc_box

# Resto del código
metricas_seleccionadas2 = ['Accelerations per 90', 'Won defensive duels per 90 (number)', 'Won aerial duels per 90 (number)', 'Forward successful passes per 90 (number)', 'xA per 90', 'Differential xG / Goals per 90', 'Interceptions per 90']
pesos2 = [0.5, 0.5, 0.25, 0.1, 0.1, 0.25, 0.25]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Accelerations per 90', 'Won defensive duels per 90 (number)', 'Won aerial duels per 90 (number)', 'Forward successful passes per 90 (number)', 'xA per 90', 'Differential xG / Goals per 90', 'Interceptions per 90']

resultado_mc_box = calcular_rendimiento2(df_mc_box, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_mc_box)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_mc, resultado_mc_box, resultado_mc_org, resultado_mc_def]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_mc_completo = df_mc.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_mc_completo.columns]
    df_mc_completo = pd.concat([df_mc_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_mc_completo.to_excel('df_mc_n2.xlsx', index=True)






