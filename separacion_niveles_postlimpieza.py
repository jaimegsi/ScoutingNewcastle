import pandas as pd
import openpyxl

#run: shift+alt+e

df = pd.read_excel("C:/Users/jaime/Documents/PycharmProjects/pythonProject1/DATOS TODAS LAS LIGAS.xlsx")
print(df)

unique_values = df['Domestic League'].unique()

print(unique_values)

n1 = df[df['Level'] == 1]
n2 = df[df['Level'] == 2]
n3 = df[df['Level'] == 3]
n4 = df[df['Level'] == 4]
n5 = df[df['Level'] == 5]

print(n1)
print(n2)
print(n3)
print(n4)
print(n5)

n1.to_excel('NIVEL1 NUEVO.xlsx', index=False)
n2.to_excel('NIVEL2 NUEVO.xlsx', index=False)
n3.to_excel('NIVEL3 NUEVO.xlsx', index=False)
n4.to_excel('NIVEL4 NUEVO.xlsx', index=False)
n5.to_excel('NIVEL5 NUEVO.xlsx', index=False)

