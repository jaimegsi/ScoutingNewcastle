import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/NIVEL5 NUEVO.xlsx")
print(n1)

# Filtramos por jugadores que hayan jugado más de 500 minutos para sacar datos más concluyentes
n1 = n1[n1['Minutes played'] > 700]
print(n1)


#Separar los frames por posiciones y perfiles
df_dfc = n1[n1['Primary position'].isin(['CB', 'LCB', 'RCB'])].copy()
df_dfc_esp = n1[n1['Primary position'].isin(['CB', 'LCB', 'RCB'])].copy()
df_dfc_dom = n1[n1['Primary position'].isin(['CB', 'LCB', 'RCB'])].copy()
df_dfc_sal = n1[n1['Primary position'].isin(['CB', 'LCB', 'RCB'])].copy()



# CENTRALES (ESPACIOS AMPLIOS)
print(df_dfc_esp)

def calcular_rendimiento(df_dfc_esp, metricas_seleccionadas, pesos, columnas_a_mantener):
    # Calcular media y desviación estándar
    means = df_dfc_esp[metricas_seleccionadas].mean()
    stds = df_dfc_esp[metricas_seleccionadas].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dfc_esp_norm = (df_dfc_esp[metricas_seleccionadas] - means) / stds

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica in enumerate(metricas_seleccionadas):
        df_dfc_esp[metrica + '_puntuacion'] = df_dfc_esp_norm[metrica] * pesos[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dfc_esp['puntuacion_total'] = df_dfc_esp[[metrica + '_puntuacion' for metrica in metricas_seleccionadas]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima = df_dfc_esp['puntuacion_total'].max()
    puntuacion_minima = df_dfc_esp['puntuacion_total'].min()

    df_dfc_esp['Rendimiento centrales espacios amplios'] = ((df_dfc_esp['puntuacion_total'] - puntuacion_minima) / (
                puntuacion_maxima - puntuacion_minima)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles = np.percentile(df_dfc_esp['Rendimiento centrales espacios amplios'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador = []
    for r in df_dfc_esp['Rendimiento centrales espacios amplios']:
        for i, p in enumerate(percentiles):
            if r <= p:
                grupo_jugador.append(i + 1)
                break
        else:
            grupo_jugador.append(10)

    # Agregar columna grupos
    df_dfc_esp['Grupo centrales espacios amplios'] = grupo_jugador

    # Agregar puntuación normalizada
    for metrica in metricas_seleccionadas:
        df_dfc_esp[metrica + '_puntuacion_norm'] = df_dfc_esp_norm[metrica]

    # Especificar columnas a mantener
    columnas_a_mantener = columnas_a_mantener + ['Rendimiento centrales espacios amplios',
                                                 'Grupo centrales espacios amplios']

    # Reorganizar las columnas del DataFrame
    df_dfc_esp = df_dfc_esp.reindex(columns=columnas_a_mantener)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dfc_esp = df_dfc_esp.round(2)

    # Ordenar el DataFrame df_dfc_esp de mayor a menor según la columna 'Rendimiento'
    df_dfc_esp = df_dfc_esp.sort_values(by='Rendimiento centrales espacios amplios', ascending=False)

    return df_dfc_esp


# Resto del código
# Define las variables necesarias: metricas_seleccionadas, pesos, columnas_a_mantener
# ...
metricas_seleccionadas = ['Won duels per 90 (number)', 'Won defensive duels per 90 (number)', 'Won offensive duels per 90 (number)', 'Successful progressive passes per 90 (number)', 'Successful long passes per 90 (number)', 'Interceptions per 90', 'Shots blocked per 90']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos = [0.5, 0.5, 0.25, 0.25, 0.25, 0.1, 0.1]

columnas_a_mantener = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Won duels per 90 (number)', 'Won defensive duels per 90 (number)', 'Won offensive duels per 90 (number)', 'Successful progressive passes per 90 (number)', 'Successful long passes per 90 (number)', 'Interceptions per 90', 'Shots blocked per 90']

# Llama a la función calcular_rendimiento
resultado_dfc_esp = calcular_rendimiento(df_dfc_esp, metricas_seleccionadas, pesos, columnas_a_mantener)

# Imprime el resultado
print(resultado_dfc_esp)


#--------------------------------------------------------------------------------------------------------------------------------------------------------
# CENTRALES (DOMINADORES AÉREOS)

def calcular_rendimiento1(df_dfc_dom, metricas_seleccionadas1, pesos1, columnas_a_mantener1):
    # Calcular media y desviación estándar
    means1 = df_dfc_dom[metricas_seleccionadas1].mean()
    stds1 = df_dfc_dom[metricas_seleccionadas1].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dfc_dom_norm = (df_dfc_dom[metricas_seleccionadas1] - means1) / stds1

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica1 in enumerate(metricas_seleccionadas1):
        df_dfc_dom[metrica1 + '_puntuacion'] = df_dfc_dom_norm[metrica1] * pesos1[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dfc_dom['puntuacion_total'] = df_dfc_dom[[metrica1 + '_puntuacion' for metrica1 in metricas_seleccionadas1]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima1 = df_dfc_dom['puntuacion_total'].max()
    puntuacion_minima1 = df_dfc_dom['puntuacion_total'].min()

    df_dfc_dom['Rendimiento centrales dominadores aéreos'] = ((df_dfc_dom['puntuacion_total'] - puntuacion_minima1) / (
                puntuacion_maxima1 - puntuacion_minima1)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles1 = np.percentile(df_dfc_dom['Rendimiento centrales dominadores aéreos'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador1 = []
    for r in df_dfc_dom['Rendimiento centrales dominadores aéreos']:
        for i, p in enumerate(percentiles1):
            if r <= p:
                grupo_jugador1.append(i + 1)
                break
        else:
            grupo_jugador1.append(10)

    # Agregar columna grupos
    df_dfc_dom['Grupo centrales dominadores aéreos'] = grupo_jugador1

    # Agregar puntuación normalizada
    for metrica1 in metricas_seleccionadas1:
        df_dfc_dom[metrica1 + '_puntuacion_norm'] = df_dfc_dom_norm[metrica1]

    # Especificar columnas a mantener
    columnas_a_mantener1 = columnas_a_mantener1 + ['Rendimiento centrales dominadores aéreos',
                                                 'Grupo centrales dominadores aéreos']

    # Reorganizar las columnas del DataFrame
    df_dfc_dom = df_dfc_dom.reindex(columns=columnas_a_mantener1)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dfc_dom = df_dfc_dom.round(2)

    # Ordenar el DataFrame df_dfc_dom de mayor a menor según la columna 'Rendimiento'
    df_dfc_dom = df_dfc_dom.sort_values(by='Rendimiento centrales dominadores aéreos', ascending=False)

    return df_dfc_dom

# Resto del código
metricas_seleccionadas1 = ['Won aerial duels per 90 (number)', 'Head goals', 'Successful defensive actions per 90', 'Interceptions per 90', 'Won defensive duels per 90 (number)', 'Won duels per 90 (number)']

# Lista de pesos correspondientes a las métricas seleccionadas
pesos1 = [0.5, 0.5, 0.25, 0.25, 0.1, 0.1]

columnas_a_mantener1 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Won aerial duels per 90 (number)', 'Head goals', 'Successful defensive actions per 90', 'Interceptions per 90', 'Won defensive duels per 90 (number)', 'Won duels per 90 (number)']

# Llama a la función calcular_rendimiento1 con df_dfc_dom
resultado_dfc_dom = calcular_rendimiento1(df_dfc_dom, metricas_seleccionadas1, pesos1, columnas_a_mantener1)

# Imprime el resultado para df_dfc_dom
print(resultado_dfc_dom)
#--------------------------------------------------------------------------------------------------------------------------------------------------------
# CENTRALES (SALIDA DE BALÓN)
def calcular_rendimiento2(df_dfc_sal, metricas_seleccionadas2, pesos2, columnas_a_mantener2):
    # Calcular media y desviación estándar
    means2 = df_dfc_sal[metricas_seleccionadas2].mean()
    stds2 = df_dfc_sal[metricas_seleccionadas2].std()

    # Normaliza los datos utilizando la normalización por z-score
    df_dfc_sal_norm = (df_dfc_sal[metricas_seleccionadas2] - means2) / stds2

    # Calcula la puntuación por estadística multiplicada por su peso
    for i, metrica2 in enumerate(metricas_seleccionadas2):
        df_dfc_sal[metrica2 + '_puntuacion'] = df_dfc_sal_norm[metrica2] * pesos2[i]

    # Calcula la puntuación total sumando las puntuaciones ponderadas por cada estadística
    df_dfc_sal['puntuacion_total'] = df_dfc_sal[[metrica2 + '_puntuacion' for metrica2 in metricas_seleccionadas2]].sum(
        axis=1)

    # Normalizar entre 0 y 10
    puntuacion_maxima2 = df_dfc_sal['puntuacion_total'].max()
    puntuacion_minima2 = df_dfc_sal['puntuacion_total'].min()

    df_dfc_sal['Rendimiento centrales salida de balón'] = ((df_dfc_sal['puntuacion_total'] - puntuacion_minima2) / (
                puntuacion_maxima2 - puntuacion_minima2)) * 10

    # Calcular los percentiles de las puntuaciones
    import numpy as np
    percentiles2 = np.percentile(df_dfc_sal['Rendimiento centrales salida de balón'], np.arange(10, 101, 10))

    # Calcular en qué grupo se encuentra cada jugador
    grupo_jugador2 = []
    for r in df_dfc_sal['Rendimiento centrales salida de balón']:
        for i, p in enumerate(percentiles2):
            if r <= p:
                grupo_jugador2.append(i + 1)
                break
        else:
            grupo_jugador2.append(10)

    # Agregar columna grupos
    df_dfc_sal['Grupo centrales salida de balón'] = grupo_jugador2

    # Agregar puntuación normalizada
    for metrica2 in metricas_seleccionadas2:
        df_dfc_sal[metrica2 + '_puntuacion_norm'] = df_dfc_sal_norm[metrica2]

    # Especificar columnas a mantener
    columnas_a_mantener2 = columnas_a_mantener2 + ['Rendimiento centrales salida de balón',
                                                 'Grupo centrales salida de balón']

    # Reorganizar las columnas del DataFrame
    df_dfc_sal = df_dfc_sal.reindex(columns=columnas_a_mantener2)

    # Eliminar las columnas con las estadísticas normalizadas y redondear los valores a dos decimales
    df_dfc_sal = df_dfc_sal.round(2)

    # Ordenar el DataFrame df_dfc_sal de mayor a menor según la columna 'Rendimiento'
    df_dfc_sal = df_dfc_sal.sort_values(by='Rendimiento centrales salida de balón', ascending=False)

    return df_dfc_sal

# Resto del código
metricas_seleccionadas2 = ['Accelerations per 90', 'Progressive runs per 90', 'Successful progressive passes per 90 (number)', 'Successful defensive actions per 90', 'Successful dribbles per 90 (number)', 'Won defensive duels per 90 (number)']
pesos2 = [0.5, 0.5, 0.5, 0.25, 0.25, 0.1]
columnas_a_mantener2 = ['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %','Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height','Weight', 'Secondary position', 'Secondary position, %','Games played', 'Minutes played', 'Accelerations per 90', 'Progressive runs per 90', 'Successful progressive passes per 90 (number)', 'Successful defensive actions per 90', 'Successful dribbles per 90 (number)', 'Won defensive duels per 90 (number)']

resultado_dfc_sal = calcular_rendimiento2(df_dfc_sal, metricas_seleccionadas2, pesos2, columnas_a_mantener2)

print(resultado_dfc_sal)

# juntar datos

# Crear una lista de dataframes a combinar
dataframes = [df_dfc, resultado_dfc_sal, resultado_dfc_dom, resultado_dfc_esp]

# Crear el dataframe 'df_lat_completo' como una copia de 'df_lat'
df_dfc_completo = df_dfc.copy()

# Iterar sobre los dataframes restantes y añadir columnas que no estén duplicadas en 'df_lat_completo'
for df in dataframes[1:]:
    new_columns = [col for col in df.columns if col not in df_dfc_completo.columns]
    df_dfc_completo = pd.concat([df_dfc_completo, df[new_columns]], axis=1)

# Exportar el dataframe a un archivo Excel (.xlsx)
df_dfc_completo.to_excel('df_dfc_n5.xlsx', index=True)





