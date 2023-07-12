import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_n1.xlsx")
n2 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_n2.xlsx")
n3 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_n3.xlsx")
n4 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_n4.xlsx")
n5 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_n5.xlsx")


df_dfc_todos = pd.concat([n1, n2, n3, n4, n5], ignore_index=True)

# Verificar el resultado
print(df_dfc_todos)

df_dfc_todos.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_dfc_todos.xlsx", index=False)