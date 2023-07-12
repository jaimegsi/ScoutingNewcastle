import pandas as pd
import openpyxl

por = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_todos.xlsx")
dfc = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_todos.xlsx")
lat = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_lat_todos.xlsx")
mc = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_todos.xlsx")
ex = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_ex_todos.xlsx")
dc = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dc_todos.xlsx")

import pandas as pd

# Columnas comunes en los DataFrames 'por', 'dfc', 'lat', 'mc', 'ex' y 'dc'
columnas_comunes = ['Unnamed: 0', 'Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %',
                                        'Age', 'Market value', 'Contract expires', 'On loan', 'Birth country', 'Birth date', 'Foot', 'Height',
                                        'Weight', 'Last club', 'Secondary position', 'Secondary position, %', 'Third position',
                                        'Third position, %', 'Passport country 1', 'Passport country 2', 'Games played', 'Minutes played',
                                        'Accelerations per 90', 'Accurate crosses, %', 'Accurate passes to final third, %',
                                        'Accurate passes to penalty area, %', 'Accurate passes, %', 'Accurate short medium passes, %',
                                        'Accurate smart passes, %', 'Aerial duels per 90', 'Aerial duels won, %', 'Assists', 'Assists per 90',
                                        'Average long pass lenght', 'Average pass lenght', 'Back passes per 90', 'Back passes to gk per 90',
                                        'Clean sheets', 'Conceded goals', 'Conceded goals per 90', 'Corners taken per 90',
                                        'Cross to goalie box per 90', 'Crosses from left per 90', 'Crosses from right per 90',
                                        'Crosses per 90', 'Deep completed crosses per 90', 'Deep completed passes per 90',
                                        'Defensive duels per 90', 'Defensive duels won, %', 'Differential xG / Goals against per 90',
                                        'Differential xG / Goals per 90', 'Direct free kicks on target, %', 'Direct free kicks taken per 90',
                                        'Dribbles per 90', 'Duels per 90', 'Duels won, %', 'Forward passes per 90',
                                        'Forward successful passes per 90 (number)', 'Fouls per 90', 'Fouls suffered per 90',
                                        'Free kicks taken per 90', 'Gk aerial duels per 90', 'Goal conversion, %', 'Goalkeeper exits per 90',
                                        'Goals', 'Goals per 90', 'Head goals', 'Head goals per 90', 'Interceptions per 90', 'Key passes per 90',
                                        'Long passes per 90', 'Non penalty goals', 'Non penalty goals per 90', 'Offensive duels per 90',
                                        'Offensive duels won, %', 'Passes per 90', 'Passes to final third per 90',
                                        'Passes to penalty area per 90', 'Penalties conversion, %', 'Penalties taken',
                                        'Possession adjusted interceptions', 'Possession adjusted tackles', 'Prevented goals',
                                        'Prevented goals per 90', 'Progressive passes per 90', 'Progressive runs per 90',
                                        'Received long passes per 90', 'Received passes per 90', 'Red cards', 'Red cards per 90', 'Saves, %',
                                        'Second assists per 90', 'Secondary assists per 90 (number)', 'Short / medium passes per 90',
                                        'Shot assists per 90', 'Shots', 'Shots against', 'Shots against per 90', 'Shots blocked per 90',
                                        'Shots on target, %', 'Shots per 90', 'Shots per gol against', 'Smart passes per 90',
                                        'Successful attacking actions per 90', 'Successful back passes, %', 'Successful crosses from left, %',
                                        'Successful crosses from right, %', 'Successful crosses per 90 (number)',
                                        'Successful defensive actions per 90', 'Successful dribbles per 90 (number)', 'Successful dribbles, %',
                                        'Successful forward passes, %', 'Successful long passes per 90 (number)', 'Successful long passes, %',
                                        'Successful passes per 90 (number)', 'Successful passes to final third per 90 (number)',
                                        'Successful passes to penalty area per 90 (number)', 'Successful progressive passes per 90 (number)',
                                        'Successful progressive passes, %', 'Successful smart passes per 90 (number)',
                                        'Successful through passes, %', 'Successful vertical passes, %', 'Tackles per 90',
                                        'Third assists per 90',  'Through passes per 90', 'Touches in the box per 90', 'Vertical passes per 90',
                                        'Won aerial duels per 90 (number)', 'Won defensive duels per 90 (number)', 'Won duels per 90 (number)',
                                        'Won offensive duels per 90 (number)', 'Yellow cards', 'Yellow cards per 90', 'xA', 'xA per 90', 'xG',
                                        'xG against', 'xG against per 90', 'xG per 90']

# Columnas adicionales en el DataFrame 'por'
columnas_por_adicionales = ['Rendimiento porteros juego de pies', 'Grupo porteros juego de pies',
                            'Rendimiento porteros acciones bajo palos', 'Grupo porteros acciones bajo palos',
                            'Rendimiento porteros dominadores de area', 'Grupo porteros dominadores de area']

# Columnas adicionales en el DataFrame 'dfc'
columnas_dfc_adicionales = ['Rendimiento centrales salida de balón', 'Grupo centrales salida de balón',
                            'Rendimiento centrales dominadores aéreos', 'Grupo centrales dominadores aéreos',
                            'Rendimiento centrales espacios amplios', 'Grupo centrales espacios amplios']

# Columnas adicionales en el DataFrame 'lat'
columnas_lat_adicionales = ['Rendimiento laterales recorridos amplios', 'Grupo laterales recorridos amplios',
                            'Rendimiento laterales asociativos', 'Grupo laterales asociativos',
                            'Rendimiento laterales posicionales', 'Grupo laterales posicionales']

# Columnas adicionales en el DataFrame 'mc'
columnas_mc_adicionales = ['Rendimiento mediocentros box-to-box', 'Grupo mediocentros box-to-box',
                           'Rendimiento mediocentros organizativos', 'Grupo mediocentros organizativos',
                           'Rendimiento mediocentros defensivos', 'Grupo mediocentros defensivos',
                           'Rendimiento mediocentros finalizadores', 'Grupo mediocentros finalizadores',
                           'Rendimiento mediocentros ofensivos asociativos', 'Grupo mediocentros ofensivos asociativos',
                           'Rendimiento mediocentros ofensivos desequilibrantes', 'Grupo mediocentros ofensivos desequilibrantes']

# Columnas adicionales en el DataFrame 'ex'
columnas_ex_adicionales = ['Rendimiento extremos desmarques espacios', 'Grupo extremos desmarques espacios',
                           'Rendimiento extremos regateadores', 'Grupo extremos regateadores',
                           'Rendimiento extremos asociativos', 'Grupo extremos asociativos']

# Columnas adicionales en el DataFrame 'dc'
columnas_dc_adicionales = ['Rendimiento delanteros espacios amplios', 'Grupo delanteros espacios amplios',
                           'Rendimiento delanteros asociativos', 'Grupo delanteros asociativos',
                           'Rendimiento delanteros referencia', 'Grupo delanteros referencia']

# Concatenar los DataFrames verticalmente
df_merged = pd.concat([por[columnas_comunes + columnas_por_adicionales],
                       dfc[columnas_comunes + columnas_dfc_adicionales],
                       lat[columnas_comunes + columnas_lat_adicionales],
                       mc[columnas_comunes + columnas_mc_adicionales],
                       ex[columnas_comunes + columnas_ex_adicionales],
                       dc[columnas_comunes + columnas_dc_adicionales]], ignore_index=True)

# Verificar el resultado
print(df_merged.shape)  # Imprimir el número de filas y columnas
print(df_merged)

df_merged = df_merged.fillna(0)

df_merged = df_merged.sort_values(['Level', 'Domestic League', 'Market value', 'Age', 'Minutes played'], ascending=[True, True, False, True, True])

df_merged = df_merged[df_merged['Domestic League'] != 0]

df_merged['Age'] = df_merged['Age'].astype(int)

df_merged = df_merged.drop('Unnamed: 0', axis=1)




df_merged.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS COMPLETOS CON RENDIMIENTO.xlsx", index=False)

