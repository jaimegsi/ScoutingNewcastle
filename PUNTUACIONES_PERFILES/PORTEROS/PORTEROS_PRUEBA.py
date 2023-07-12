import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_n1.xlsx")
n2 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_n2.xlsx")
n3 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_n3.xlsx")
n4 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_n4.xlsx")
n5 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_n5.xlsx")


df_lat_todos = pd.concat([n1, n2, n3, n4, n5], ignore_index=True)

# Verificar el resultado
print(df_lat_todos)

df_lat_todos.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_por_todos.xlsx", index=False)