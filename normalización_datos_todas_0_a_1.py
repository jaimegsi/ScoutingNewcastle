import requests
import pandas as pd
from pandas import json_normalize
import json
from sqlalchemy import create_engine
from datetime import datetime,date
from datetime import timedelta
from tqdm import tqdm
from sklearn.preprocessing import MinMaxScaler

df = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS COMPLETOS CON RENDIMIENTO.xlsx")

newcastle = df[df['Team'] == 'Newcastle United']


df_n1 = df.loc[df['Level'] == 1]
df_n2 = df.loc[df['Level'] == 2]
df_n3 = df.loc[df['Level'] == 3]
df_n4 = df.loc[df['Level'] == 4]
df_n5 = df.loc[df['Level'] == 5]
# Lista de columnas a normalizar
columnas_a_normalizar = ['Accelerations per 90', 'Accurate crosses, %', 'Accurate passes to final third, %',
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
                                        'xG against', 'xG against per 90', 'xG per 90', 'Rendimiento porteros juego de pies', 'Grupo porteros juego de pies',
                            'Rendimiento porteros acciones bajo palos', 'Grupo porteros acciones bajo palos',
                            'Rendimiento porteros dominadores de area', 'Grupo porteros dominadores de area', 'Rendimiento centrales salida de balón', 'Grupo centrales salida de balón',
                            'Rendimiento centrales dominadores aéreos', 'Grupo centrales dominadores aéreos',
                            'Rendimiento centrales espacios amplios', 'Grupo centrales espacios amplios', 'Rendimiento laterales recorridos amplios', 'Grupo laterales recorridos amplios',
                            'Rendimiento laterales asociativos', 'Grupo laterales asociativos',
                            'Rendimiento laterales posicionales', 'Grupo laterales posicionales', 'Rendimiento mediocentros box-to-box', 'Grupo mediocentros box-to-box',
                           'Rendimiento mediocentros organizativos', 'Grupo mediocentros organizativos',
                           'Rendimiento mediocentros defensivos', 'Grupo mediocentros defensivos',
                           'Rendimiento mediocentros finalizadores', 'Grupo mediocentros finalizadores',
                           'Rendimiento mediocentros ofensivos asociativos', 'Grupo mediocentros ofensivos asociativos',
                           'Rendimiento mediocentros ofensivos desequilibrantes', 'Grupo mediocentros ofensivos desequilibrantes', 'Rendimiento extremos desmarques espacios', 'Grupo extremos desmarques espacios',
                           'Rendimiento extremos regateadores', 'Grupo extremos regateadores',
                           'Rendimiento extremos asociativos', 'Grupo extremos asociativos', 'Rendimiento delanteros espacios amplios', 'Grupo delanteros espacios amplios',
                           'Rendimiento delanteros asociativos', 'Grupo delanteros asociativos',
                           'Rendimiento delanteros referencia', 'Grupo delanteros referencia']

# Crear el objeto MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 1))

# Normalizar las columnas seleccionadas en el DataFrame
df_n1.loc[:, columnas_a_normalizar] = scaler.fit_transform(df_n1[columnas_a_normalizar])
df_n2.loc[:, columnas_a_normalizar] = scaler.fit_transform(df_n2[columnas_a_normalizar])
df_n3.loc[:, columnas_a_normalizar] = scaler.fit_transform(df_n3[columnas_a_normalizar])
df_n4.loc[:, columnas_a_normalizar] = scaler.fit_transform(df_n4[columnas_a_normalizar])
df_n5.loc[:, columnas_a_normalizar] = scaler.fit_transform(df_n5[columnas_a_normalizar])

# Concatenar los dataframes en uno solo
df_n12345 = pd.concat([df_n1, df_n2, df_n3, df_n4, df_n5])

# Restablecer el índice del dataframe resultante
df_n12345.reset_index(drop=True, inplace=True)

df_n12345.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS NORMALIZADOS COMPLETOS CON RENDIMIENTO.xlsx", index=False)


df_n12345['Index'] = df_n12345.apply(lambda row: '.'.join([str(row['Full name']), str(row['Team']), str(row['Domestic League']), str(row['Primary position'])]), axis=1)

final_df = pd.DataFrame()
for i in df_n12345.columns.to_list():
    if i != "Index" and df_n12345[i].dtype != object:
        new_df = pd.DataFrame()
        new_df["Measure"] = df_n12345[i]
        new_df["Dimension"] = i
        new_df["Index"] = df_n12345["Index"]
        new_df["Index2"] = df_n12345["Index"] + "." + new_df["Dimension"]
        new_df["Full name"] = df_n12345["Full name"]
        new_df["Link"] = "Link"
        final_df = pd.concat([final_df, new_df])
final_df = final_df.dropna()

final_df.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS NORMALIZADOS.xlsx", index=False)
