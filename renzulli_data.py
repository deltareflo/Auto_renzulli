import pandas as pd

url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQWAa4KZbz5kLsHDglpO30snn27IIQTP914oZNcYlUaHRlG7IXFe4SEKFRq6kc8mqRkwDQA6Y0kcpFY/pub?output=csv"
df = pd.read_csv(url)

#seleccionamos solo las columnas a modificar
df=df.iloc[:, 3:]
