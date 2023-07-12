import pandas as pd
import openpyxl

n1 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_n1.xlsx")
n2 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_n2.xlsx")
n3 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_n3.xlsx")
n4 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_n4.xlsx")
n5 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_n5.xlsx")
n11 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc1_n1.xlsx")
n21 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc1_n2.xlsx")
n31 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc1_n3.xlsx")
n41 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc1_n4.xlsx")
n51 = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc1_n5.xlsx")



n1_unido = pd.merge(n1, n11, on=list(set(n1.columns) & set(n11.columns)))
n2_unido = pd.merge(n2, n21, on=list(set(n2.columns) & set(n21.columns)))
n3_unido = pd.merge(n3, n31, on=list(set(n3.columns) & set(n31.columns)))
n4_unido = pd.merge(n4, n41, on=list(set(n4.columns) & set(n41.columns)))
n5_unido = pd.merge(n5, n51, on=list(set(n5.columns) & set(n51.columns)))



df_mc_todos = pd.concat([n1_unido, n2_unido, n3_unido, n4_unido, n5_unido], ignore_index=True)

# Verificar el resultado
print(df_mc_todos)

df_mc_todos.to_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/df_mc_todos.xlsx", index=False)