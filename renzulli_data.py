import pandas as pd

#Definimos funciones a utilizar

#Recodifica las variables de una columna categórica a numérica
def transforma_a_numero(x):
    if x=="Nunca":
        return 1
    elif x=="Muy raramente":
        return 2
    elif x=="Raramente":
        return 3
    elif x=="De vez en cuando":
        return 4
    elif x=="Frecuentemente":
        return 5
    else:
        return 6
#Con esta función pasamos a todas las columnas del dataframe la función transforma_a_numero
def recodifica_var(df_columns):
    for i in range(df_columns):
        df2.iloc[:,i]= df2.iloc[:,i].apply(transforma_a_numero)
    return df2

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQWAa4KZbz5kLsHDglpO30snn27IIQTP914oZNcYlUaHRlG7IXFe4SEKFRq6kc8mqRkwDQA6Y0kcpFY/pub?output=csv"
df = pd.read_csv(url)

#seleccionamos solo las columnas a modificar que en este caso empieza en la cuarta columna
df=df.iloc[:, 3:]
#Generamos una copia
df2= df
#Recategorizamos todas las columnas
df2= recodifica_var(len(df2.columns))


