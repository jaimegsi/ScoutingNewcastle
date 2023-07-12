import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/tfm/Nivel1.xlsx")
n2 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/tfm/Nivel2.xlsx")
n3 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/tfm/Nivel3.xlsx")
n4 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/tfm/Nivel4.xlsx")
n5 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/tfm/Nivel5.xlsx")

print(n3)
# Añadir columna nivel
n1['Level'] = 1
n2['Level'] = 2
n3['Level'] = 3
n4['Level'] = 4
n5['Level'] = 5
print(n5)

dataf = [n1, n2, n3, n4, n5]
df = pd.concat(dataf)

print(df.columns)

columnas_eliminar = ['id', 'current_team_logo', 'passport_country_codes1', 'passport_country_codes2', 'birth_country_code', 'image', 'positions', 'current_team_color', 'birth_day', 'positions1', 'positions2', 'positions3', 'passport_country_codes', 'passport_country_names']

df = df.drop(columnas_eliminar, axis=1)
print(df)

# cambio nombres columnas
mapeo_nombres = {
    'successful_forward_passes_percent': 'Successful forward passes, %',
    'fouls_avg': 'Fouls per 90',
    'last_club_name': 'Last club',
    'successful_vertical_passes_percent': 'Successful vertical passes, %',
    'dribbles_avg': 'Dribbles per 90',
    'back_pass_to_gk_avg': 'Back passes to gk per 90',
    'forward_passes_avg': 'Forward passes per 90',
    'deep_completed_cross_avg': 'Deep completed crosses per 90',
    'successful_attacking_actions_avg': 'Successful attacking actions per 90',
    'accelerations_avg': 'Accelerations per 90',
    'minutes_on_field': 'Minutes played',
    'through_passes_avg': 'Through passes per 90',
    'height': 'Height',
    'goals': 'Goals',
    'market_value': 'Market value',
    'foul_suffered_avg': 'Fouls suffered per 90',
    'accurate_passes_to_final_third_percent': 'Accurate passes to final third, %',
    'defensive_duels_won': 'Defensive duels won, %',
    'primary_position_percent': 'Primary position, %',
    'shots_avg': 'Shots per 90',
    'full_name': 'Full name',
    'aerial_duels_won': 'Aerial duels won, %',
    'back_passes_avg': 'Back passes per 90',
    'shots': 'Shots',
    'progressive_run_avg': 'Progressive runs per 90',
    'successful_through_passes_percent': 'Successful through passes, %',
    'received_long_pass_avg': 'Received long passes per 90',
    'successful_dribbles_percent': 'Successful dribbles, %',
    'crosses_avg': 'Crosses per 90',
    'duels_avg': 'Duels per 90',
    'successful_cross_from_left_percent': 'Successful crosses from left, %',
    'domestic_competition_name': 'Domestic League',
    'accurate_short_medium_pass_percent': 'Accurate short medium passes, %',
    'key_passes_avg': 'Key passes per 90',
    'pre_assist_avg': 'Second assists per 90',
    'xg_shot': 'xG',
    'non_penalty_goal': 'Non penalty goals',
    'foot': 'Foot',
    'total_matches': 'Games played',
    'defensive_duels_avg': 'Defensive duels per 90',
    'short_medium_pass_avg': 'Short / medium passes per 90',
    'long_passes_avg': 'Long passes per 90',
    'tackle_avg': 'Tackles per 90',
    'passes_avg': 'Passes per 90',
    'cross_from_right_avg': 'Crosses from right per 90',
    'conceded_goals': 'Conceded goals',
    'direct_free_kicks_taken_avg': 'Direct free kicks taken per 90',
    'deep_completed_pass_avg': 'Deep completed passes per 90',
    'passes_to_final_third_avg': 'Passes to final third per 90',
    'shots_against': 'Shots against',
    'direct_free_kicks_on_target_percent': 'Direct free kicks on target, %',
    'offensive_duels_won': 'Offensive duels won, %',
    'smart_passes_avg': 'Smart passes per 90',
    'penalties_conversion_percent': 'Penalties conversion, %',
    'free_kicks_taken_avg': 'Free kicks taken per 90',
    'aerial_duels_avg': 'Aerial duels per 90',
    'cross_to_goalie_box_avg': 'Cross to goalie box per 90',
    'birth_date': 'Birth date',
    'yellow_cards_avg': 'Yellow cards per 90',
    'pre_pre_assist_avg': 'Third assists per 90',
    'accurate_passes_percent': 'Accurate passes, %',
    'xg_shot_avg': 'xG per 90',
    'xg_assist': 'xA',
    'duels_won': 'Duels won, %',
    'successful_long_passes_percent': 'Successful long passes, %',
    'assists_avg': 'Assists per 90',
    'accurate_crosses_percent': 'Accurate crosses, %',
    'on_loan': 'On loan',
    'current_team_name': 'Team',
    'yellow_cards': 'Yellow cards',
    'weight': 'Weight',
    'possession_adjusted_interceptions': 'Possession adjusted interceptions',
    'offensive_duels_avg': 'Offensive duels per 90',
    'pass_to_penalty_area_avg': 'Passes to penalty area per 90',
    'cross_from_left_avg': 'Crosses from left per 90',
    'accurate_smart_passes_percent': 'Accurate smart passes, %',
    'penalties_taken': 'Penalties taken',
    'red_cards_avg': 'Red cards per 90',
    'head_goals': 'Head goals',
    'progressive_pass_avg': 'Progressive passes per 90',
    'received_pass_avg': 'Received passes per 90',
    'name': 'Name',
    'average_pass_length': 'Average pass lenght',
    'secondary_position_percent': 'Secondary position, %',
    'successful_progressive_pass_percent': 'Successful progressive passes, %',
    'xg_save_avg': 'xG against per 90',
    'successful_back_passes_percent': 'Successful back passes, %',
    'successful_defensive_actions_avg': 'Successful defensive actions per 90',
    'possession_adjusted_tackle': 'Possession adjusted tackles',
    'corners_taken_avg': 'Corners taken per 90',
    'shot_assists_avg': 'Shot assists per 90',
    'clean_sheets': 'Clean sheets',
    'red_cards': 'Red cards',
    'shot_block_avg': 'Shots blocked per 90',
    'head_goals_avg': 'Head goals per 90',
    'xg_save': 'xG against',
    'interceptions_avg': 'Interceptions per 90',
    'assists': 'Assists',
    'primary_position': 'Primary position',
    'goal_conversion_percent': 'Goal conversion, %',
    'average_long_pass_length': 'Average long pass lenght',
    'successful_cross_from_right_percent': 'Successful crosses from right, %',
    'save_percent': 'Saves, %',
    'goals_avg': 'Goals per 90',
    'passport_country_names1': 'Passport country 1',
    'passport_country_names2': 'Passport country 2',
    'contract_expires': 'Contract expires',
    'accurate_pass_to_penalty_area_percent': 'Accurate passes to penalty area, %',
    'vertical_passes_avg': 'Vertical passes per 90',
    'non_penalty_goal_avg': 'Non penalty goals per 90',
    'shots_on_target_percent': 'Shots on target, %',
    'xg_assist_avg': 'xA per 90',
    'touch_in_box_avg': 'Touches in the box per 90',
    'age': 'Age',
    'third_position_percent': 'Third position, %',
    'birth_country_name': 'Birth country',
    'third_position': 'Third position',
    'secondary_position': 'Secondary position',
    'prevented_goals': 'Prevented goals',
    'goalkeeper_exits_avg': 'Goalkeeper exits per 90',
    'conceded_goals_avg': 'Conceded goals per 90',
    'gk_aerial_duels_avg': 'Gk aerial duels per 90',
    'prevented_goals_avg': 'Prevented goals per 90',
    'shots_against_avg': 'Shots against per 90'
     }

df.columns = [mapeo_nombres.get(col, col) for col in df.columns]


df['Primary position'] = df['Primary position'].replace({'RCMF3': 'RCMF', 'RCB3': 'RCB', 'LCMF3': 'LCMF', 'LCB3': 'LCB', 'RB5': 'RB', 'LB5': 'LB'})
df['Secondary position'] = df['Secondary position'].replace({'RCMF3': 'RCMF', 'RCB3': 'RCB', 'LCMF3': 'LCMF', 'LCB3': 'LCB', 'RB5': 'RB', 'LB5': 'LB'})
df['Third position'] = df['Third position'].replace({'RCMF3': 'RCMF', 'RCB3': 'RCB', 'LCMF3': 'LCMF', 'LCB3': 'LCB', 'RB5': 'RB', 'LB5': 'LB'})

#Crear nuevas métricas
df['Differential xG / Goals against per 90'] = df['xG against per 90'] - df['Conceded goals per 90']
df['Shots per gol against'] = df['Shots against per 90'] / df['Conceded goals per 90']
df['Differential xG / Goals per 90'] = df['Goals per 90'] - df['xG per 90']
df['Secondary assists per 90 (number)'] = df['Second assists per 90'] + df['Third assists per 90']
df['Successful long passes per 90 (number)'] = df['Long passes per 90'] * (df['Successful long passes, %'] / 100)
df['Successful passes per 90 (number)'] = df['Passes per 90'] * (df['Accurate passes, %'] / 100)
df['Successful crosses per 90 (number)'] = df['Crosses per 90'] * (df['Accurate crosses, %'] / 100)
df['Successful passes to penalty area per 90 (number)'] = df['Passes to penalty area per 90'] * (df['Accurate passes to penalty area, %'] / 100)
df['Won defensive duels per 90 (number)'] = df['Defensive duels per 90'] * (df['Defensive duels won, %'] / 100)
df['Won offensive duels per 90 (number)'] = df['Offensive duels per 90'] * (df['Offensive duels won, %'] / 100)
df['Won aerial duels per 90 (number)'] = df['Aerial duels per 90'] * (df['Aerial duels won, %'] / 100)
df['Successful progressive passes per 90 (number)'] = df['Progressive passes per 90'] * (df['Successful progressive passes, %'] / 100)
df['Won duels per 90 (number)'] = df['Duels per 90'] * (df['Duels won, %'] / 100)
df['Forward successful passes per 90 (number)'] = df['Forward passes per 90'] * (df['Successful forward passes, %'] / 100)
df['Successful passes to final third per 90 (number)'] = df['Passes to final third per 90'] * (df['Accurate passes to final third, %'] / 100)
df['Successful dribbles per 90 (number)'] = df['Dribbles per 90'] * (df['Successful dribbles, %'] / 100)
df['Successful smart passes per 90 (number)'] = df['Smart passes per 90'] * (df['Accurate smart passes, %'] / 100)

df_reorder = df.reindex(columns=['Full name', 'Name', 'Team', 'Domestic League', 'Level', 'Primary position', 'Primary position, %',
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
                                        'xG against', 'xG against per 90', 'xG per 90'])


df_reorder = df_reorder[df_reorder['Minutes played'] > 700]


# Filtrar los datos por el equipo 'Villarreal'
filtro_villarreal = df_reorder['Team'] == 'Villarreal'
df_reorder.loc[filtro_villarreal, 'Domestic League'] = 'LaLiga'

df_reorder.loc[(df_reorder['Team'] == 'Arsenal') & (df_reorder['Domestic League'] == 'Liga Profesional de Fútbol'), 'Level'] = 3

df_reorder.loc[(df_reorder['Domestic League'] == 'Premier League') & (df_reorder['Level'] == 3), 'Domestic League'] = 'Russian Premier League'

df_reorder.loc[(df_reorder['Domestic League'] == 'Bundesliga') & (df_reorder['Level'] == 3), 'Domestic League'] = 'Bundesliga (Austria)'

# Lista de valores a eliminar
valores_a_eliminar = ['National 2', 'Qatar Stars League', 'Segunda Division RFEF', 'Division 1', 'Liga Pro', 'Liga Revelação Sub 23', 'National 1', 'Pro League', 'Segunda B', 'Segunda Liga',
                      '1. Division', '1. HNL', '1. Lig', '1. Liga Classic', '1. Liga Promotion', '3. Liga', 'Arabian Gulf League', 'Botola Pro', 'Campionato Primavera 2',
                      'División de Honor Juvenil', 'Erovnuli Liga', 'FNL', 'FNL 2', 'First League', "Ligat ha'Al", 'NB I', 'National Division 1', 'National League',
                      'National League N / S', 'New South Wales NPL', 'Play-offs 1/2', 'Premier Division', 'Premijer Liga', 'Primera Division RFEF', 'Primera Division',
                      'Primera División', 'Professional Development League', 'Regionalliga', 'Reserve League', 'Serie C', 'Tercera Division', 'Tweede Divisie', 'Western Australia NPL',
                      'Youth Championship', 'U17 Bundesliga', 'U18 Premier League', 'U19 Ligaen', 'U20 League', 'NaN']
df_reorder = df_reorder[~df_reorder['Domestic League'].isin(valores_a_eliminar)]


# Ordenar el dataframe df_reorder
df_reorder = df_reorder.sort_values(by=['Level', 'Domestic League', 'Team', 'Minutes played', 'Primary position'])
print(df_reorder)


# REORDENAR NIVELES
# LIGA A LIGA
ligas_n1 = ['Premier League', 'LaLiga', 'Bundesliga', 'Serie A', 'Ligue 1']
filtro_ligasn1 = df_reorder['Domestic League'].isin(ligas_n1)
df_reorder.loc[filtro_ligasn1, 'Level'] = 1

ligas_n2 = ['Eredivisie', 'Primeira Liga', 'First Division A', 'Bundesliga (Austria)', 'Superliga', 'MLS', 'Championship',
            'Liga Profesional de Fútbol', 'Premiership']
filtro_ligasn2 = df_reorder['Domestic League'].isin(ligas_n2)
df_reorder.loc[filtro_ligasn2, 'Level'] = 2

ligas_n3 = ['Süper Lig', 'Liga MX', 'Russian Premier League', 'Super League',
            'Ligue 2', 'Eliteserien', 'Premier League 2 Division One', 'Premier League 2 Division Two']
filtro_ligasn3 = df_reorder['Domestic League'].isin(ligas_n3)
df_reorder.loc[filtro_ligasn3, 'Level'] = 3

ligas_n4 = ['Segunda División', 'Serie B', '2. Bundesliga',
            'Allsvenskan', 'League One']
filtro_ligasn4 = df_reorder['Domestic League'].isin(ligas_n4)
df_reorder.loc[filtro_ligasn4, 'Level'] = 4

ligas_n5 = ['J1 League', 'A-League', 'USL Championship', 'PSL', 'CSL', 'League Two']
filtro_ligasn5 = df_reorder['Domestic League'].isin(ligas_n5)
df_reorder.loc[filtro_ligasn5, 'Level'] = 5

############ RETOQUES
# sturm
cambio_sturm = df_reorder['Team'] == 'Sturm Graz'
df_reorder.loc[cambio_sturm, 'Domestic League'] = 'Bundesliga (Austria)'
df_reorder.loc[cambio_sturm, 'Level'] = 2

#khimki
cambio_khimki = df_reorder['Team'] == 'Khimki'
df_reorder.loc[cambio_khimki, 'Domestic League'] = 'Russian Premier League'
df_reorder.loc[cambio_khimki, 'Level'] = 3

# equipos brasil
equipos_br = ['América Mineiro', 'Athletico Paranaense' ,'Atlético Mineiro', 'Bahia', 'Botafogo', 'Coritiba',
              'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Vasco da Gama', 'Internacional', 'Grêmio',
              'Corinthians', 'Palmeiras', 'Red Bull Bragantino', 'Santos', 'São Paulo']
filtro_equipos_br = df_reorder['Team'].isin(equipos_br)
df_reorder.loc[filtro_equipos_br, 'Domestic League'] = 'Serie A (Brasil)'
df_reorder.loc[filtro_equipos_br, 'Level'] = 2

# equipos bundesliga
equipos_ger = ['Augsburg', 'Bayer Leverkusen', 'Bayern München', 'Bochum', 'Borussia Dortmund', "Borussia M'gladbach",
               'Eintracht Frankfurt', 'Freiburg', 'Hertha BSC', 'Hoffenheim', 'Köln', 'Mainz 05', 'RB Leipzig', 'Schalke 04',
               'Stuttgart', 'Union Berlin', 'Werder Bremen', 'Wolfsburg']
filtro_equipos_ger = df_reorder['Team'].isin(equipos_ger)
df_reorder.loc[filtro_equipos_ger, 'Domestic League'] = 'Bundesliga'
df_reorder.loc[filtro_equipos_ger, 'Level'] = 1


# equipos a eliminar
equipos_eliminar = ['Ayr United', 'Dundee', 'Hamilton Academical', "Queen's Park", 'Universitatea Cluj', 'Club Brugge II',
                    'Inter Miami II', 'Penang', 'Volendam U19']
df_reorder = df_reorder[~df_reorder['Team'].isin(equipos_eliminar)]

# premier rusos
filtro_russian_premier = (df_reorder['Domestic League'] == 'Russian Premier League') & (df_reorder['Team'].isin(['Arsenal', 'Aston Villa', 'Bournemouth', 'Everton', 'Leeds United', 'Liverpool',
                                                                                                                 'Leicester City', 'Manchester City', 'Manchester United', 'Newcastle United',
                                                                                                                 'Nottingham Forest', 'Southampton', 'Wolverhampton Wanderers']))
df_reorder.loc[filtro_russian_premier, 'Domestic League'] = 'Premier League'
df_reorder.loc[filtro_russian_premier, 'Level'] = 1

# cambiar nombre liga suiza
df_reorder['Domestic League'] = df_reorder['Domestic League'].replace('Superliga', 'Danish Superliga')

# super league
equipos_superleague = df_reorder.loc[df_reorder['Domestic League'] == 'Super League', 'Team'].unique()
for equipo in equipos_superleague:
    print(equipo)

# equipos suizos
equipos_sw = ['Basel', 'Grasshopper', 'Lamia', 'Lugano', 'Luzern', 'Servette', 'Sion', 'St. Gallen', 'Winterthur', 'Young Boys', 'Zürich']
filtro_equipos_sw = df_reorder['Team'].isin(equipos_sw)
df_reorder.loc[filtro_equipos_sw, 'Domestic League'] = 'Swiss Super League'
df_reorder.loc[filtro_equipos_sw, 'Level'] = 2

# equipos griegos
equipos_gre = ['Olympiacos Piraeus', 'AEK Athens', 'Aris', 'Asteras Tripolis', 'Atromitos',
               'Ionikos', 'Levadiakos', 'OFI', 'PAOK', 'PAS Giannina', 'Panathinaikos', 'Panetolikos FC', 'Volos NFC']
filtro_equipos_gre = df_reorder['Team'].isin(equipos_gre)
df_reorder.loc[filtro_equipos_gre, 'Domestic League'] = 'Super League (Greece)'
df_reorder.loc[filtro_equipos_gre, 'Level'] = 3




# Obtener los diferentes valores de la columna 'Domestic League'
# Agrupar por 'Domestic League' y 'Level' y contar las ocurrencias
domestic_leagues = df_reorder.groupby(['Domestic League', 'Team', 'Level']).size().reset_index()
domestic_leagues = domestic_leagues.sort_values(by=['Level', 'Domestic League', 'Team'])
print(domestic_leagues)





df_reorder = df_reorder.sort_values(['Level', 'Domestic League', 'Market value', 'Age', 'Minutes played'], ascending=[True, True, False, True, True])

print(df_reorder)


df_reorder.to_excel('DATOS TODAS LAS LIGAS.xlsx', index=False)




