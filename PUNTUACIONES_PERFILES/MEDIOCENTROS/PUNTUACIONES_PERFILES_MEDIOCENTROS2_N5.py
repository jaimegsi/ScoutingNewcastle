import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL5 NUEVO.xlsx")
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

# MEDIOCENTROS (OFENSIVO ASOCIATIVO)
print(df_mc_aso)

def calcular_rendimiento(df_mc_aso, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_mc_aso[metricas_seleccionadas].mean()
    stds = df_mc_aso[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_aso_norm = (df_mc_aso[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_mc_aso[metrica + '_puntuacion'] = df_mc_aso_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_aso['puntuacion_total'] = df_mc_aso[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_mc_aso['puntuacion_total'].max()
    puntuacion_minima = df_mc_aso['puntuacion_total'].min()

    df_mc_aso['Rendimiento mediocentros ofensivos asociativos'] = ((df_mc_aso['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles = np.percentile(df_mc_aso['Rendimiento mediocentros ofensivos asociativos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_mc_aso['Rendimiento mediocentros ofensivos asociativos']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_mc_aso['Grupo mediocentros ofensivos asociativos'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_mc_aso[metrica + '_puntuacion_norm'] = df_mc_aso_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento mediocentros ofensivos asociativos',
                                                 'Grupo mediocentros ofensivos asociativos']

    # Reorganizar las columnas del DataFrame
    df_mc_aso = df_mc_aso.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_aso = df_mc_aso.round(2)

    # Ordenar el DataFrame df_mc_aso de mayor a menor según la columna 'Rendimiento'
    df_mc_aso = df_mc_aso.sort_values(by='Rendimiento mediocentros ofensivos asociativos', ascending=False)

    return df_mc_aso

# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Successful smart passes per 90 (number)', 'Successful passes to final third per 90 (number)', 'Key passes per 90', 'Successful passes to penalty area per 90 (number)', 'xA per 90', 'Second assists per 90', 'Third assists per 90', 'Received passes per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.25, 0.5, 0.5, 0.25, 0.1, 0.1, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful smart passes per 90 (number)', 'Successful passes to final third per 90 (number)', 'Key passes per 90', 'Successful passes to penalty area per 90 (number)', 'xA per 90', 'Second assists per 90', 'Third assists per 90', 'Received passes per 90']

# Llama a la función calcular_rendimiento
resultado_mc_aso = calcular_rendimiento(df_mc_aso, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_mc_aso)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# MEDIOCENTROS (OFENSIVOS DESEQUILIBRANTES)

def calcular_rendimiento1(df_mc_des, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_mc_des[metricas_seleccionadas1].mean()
    stds1 = df_mc_des[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_des_norm = (df_mc_des[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_mc_des[metrica1 + '_puntuacion'] = df_mc_des_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_des['puntuacion_total'] = df_mc_des[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_mc_des['puntuacion_total'].max()
    puntuacion_minima1 = df_mc_des['puntuacion_total'].min()

    df_mc_des['Rendimiento mediocentros ofensivos desequilibrantes'] = ((df_mc_des['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_mc_des['Rendimiento mediocentros ofensivos desequilibrantes'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_mc_des['Rendimiento mediocentros ofensivos desequilibrantes']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_mc_des['Grupo mediocentros ofensivos desequilibrantes'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_mc_des[metrica1 + '_puntuacion_norm'] = df_mc_des_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento mediocentros ofensivos desequilibrantes',
                                                 'Grupo mediocentros ofensivos desequilibrantes']

    # Reorganizar las columnas del DataFrame
    df_mc_des = df_mc_des.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_des = df_mc_des.round(2)

    # Ordenar el DataFrame df_mc_des de mayor a menor según la columna 'Rendimiento'
    df_mc_des = df_mc_des.sort_values(by='Rendimiento mediocentros ofensivos desequilibrantes', ascending=False)

    return df_mc_des

# Resto del código
metricas_seleccionadas1 = ['Successful dribbles per 90 (number)', 'Progressive runs per 90', 'Accelerations per 90', 'Differential xG / Goals per 90', 'Second assists per 90', 'Third assists per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.5, 0.5, 0.5, 0.25, 0.1, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Successful dribbles per 90 (number)', 'Progressive runs per 90', 'Accelerations per 90', 'Differential xG / Goals per 90', 'Key passes per 90', 'Second assists per 90', 'Third assists per 90']

# Llama a la función calcular_rendimiento1 con df_mc_des
resultado_mc_des = calcular_rendimiento1(df_mc_des, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_mc_des
print(resultado_mc_des)

#--------------------------------------------------------------------------------------------------------------------------------------------------------
# MEDIOCENTROS (OFENSIVO FINALIZADOR)

def calcular_rendimiento2(df_mc_fin, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_mc_fin[metricas_seleccionadas2].mean()
    stds2 = df_mc_fin[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_mc_fin_norm = (df_mc_fin[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_mc_fin[metrica2 + '_puntuacion'] = df_mc_fin_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_mc_fin['puntuacion_total'] = df_mc_fin[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_mc_fin['puntuacion_total'].max()
    puntuacion_minima2 = df_mc_fin['puntuacion_total'].min()

    df_mc_fin['Rendimiento mediocentros finalizadores'] = ((df_mc_fin['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_mc_fin['Rendimiento mediocentros finalizadores'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_mc_fin['Rendimiento mediocentros finalizadores']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_mc_fin['Grupo mediocentros finalizadores'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_mc_fin[metrica2 + '_puntuacion_norm'] = df_mc_fin_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento mediocentros finalizadores',
                                                 'Grupo mediocentros finalizadores']

    # Reorganizar las columnas del DataFrame
    df_mc_fin = df_mc_fin.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_mc_fin = df_mc_fin.round(2)

    # Ordenar el DataFrame df_mc_fin de mayor a menor según la columna 'Rendimiento'
    df_mc_fin = df_mc_fin.sort_values(by='Rendimiento mediocentros finalizadores', ascending=False)

    return df_mc_fin

# Resto del código
metricas_seleccionadas2 = ['Differential xG / Goals per 90', 'Successful attacking actions per 90', 'Goal conversion, %', 'Shots per 90', 'xG per 90', 'Won offensive duels per 90 (number)', 'Goals per 90']
pesos2 = [0.25, 0.5, 0.5, 0.25, 0.1, 0.1, 0.25]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Differential xG / Goals per 90', 'Successful attacking actions per 90', 'Goal conversion, %', 'Shots per 90', 'xG per 90', 'Won offensive duels per 90 (number)', 'Goals per 90']

resultado_mc_fin = calcular_rendimiento2(df_mc_fin, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_mc_fin)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_mc, resultado_mc_fin, resultado_mc_aso, resultado_mc_des]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_mc_completo = df_mc.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_mc_completo.columns]
    df_mc_completo = pd.concat([df_mc_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_mc_completo.to_excel('df_mc1_n5.xlsx', index=True)






