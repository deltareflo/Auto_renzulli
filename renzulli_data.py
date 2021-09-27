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

#Se declara la variable url con el link del google sheet
url = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQWAa4KZbz5kLsHDglpO30snn27IIQTP914oZNcYlUaHRlG7IXFe4SEKFRq6kc8mqRkwDQA6Y0kcpFY/pub?output=csv"
#Se lee el archivo
df = pd.read_csv(url)

#seleccionamos solo las columnas a modificar que en este caso empieza en la cuarta columna
df1=df.iloc[:, 3:]
#Generamos una copia (este paso se podría saltar si no surge incovenientes)
df2= df1
#Recategorizamos todas las columnas
df2= recodifica_var(len(df2.columns))

#Creamos un diccionario con los puntajes directos según cada dimensión para posteriormente crear un nuevo dataframe que se podrá anexar a df2
#Tiene el sistema key:values. El key es el nombre de la columna a crear y el value se obtiene de seleccionar un rango de columnas con el metodo iloc para posteriormente
#sumar por fila con el metodo sum. La sección axis=1 indica que se va a generar una columna nueva con los resultados de la suma
punt_directo = {"PD aprendizaje":df2.iloc[:,:11].sum(axis=1),
             "PD creatividad": df2.iloc[:,11:20].sum(axis=1),
             "PD motivacion": df2.iloc[:,20:31].sum(axis=1),
             "PD Liderazgo": df2.iloc[:,31:38].sum(axis=1),
             "PD artistica": df2.iloc[:,38:49].sum(axis=1),
             "PD musical": df2.iloc[:,49:56].sum(axis=1),
             "PD dramatica": df2.iloc[:,56:66].sum(axis=1),
             "PD comunicación-precisión": df2.iloc[:,66:77].sum(axis=1),
             "PD comunicación-expresión": df2.iloc[:,77:81].sum(axis=1),
             "PD planificación": df2.iloc[:,81:96].sum(axis=1)}
#Generamos el dataframe solamente con los puntajes directos
df3 = pd.DataFrame(punt_directo)
#Creamos un diccionario en base a los puntajes directos con los porcentajes según cada dimensión para posteriormente crear un nuevo dataframe que se podrá anexar a df2
porcentaje= {"Pc aprendizaje": (df3["PD aprendizaje"]/66)*100,
             "Pc creatividad": (df3["PD creatividad"]/54)*100,
             "Pc motivacion": (df3["PD motivacion"]/66)*100,
             "Pc Liderazgo": (df3["PD Liderazgo"]/42)*100,
             "Pc artistica": (df3["PD artistica"]/66)*100,
             "Pc musical": (df3["PD musical"]/42)*100,
             "Pc dramatica": (df3["PD dramatica"]/60)*100,
             "Pc comunicación-precisión": (df3["PD comunicación-precisión"]/66)*100,
             "Pc comunicación-expresión": (df3["PD comunicación-expresión"]/24)*100,
             "Pc planificación": (df3["PD planificación"]/90)*100}
#Generamos el dataframe solamente con los porcentajes (capaz se pueda redondear o dejar así no más)
df4 = pd.DataFrame(porcentaje)

#Unimos los dataframes para las 215 columnas
df5= pd.concat([df,df2,df3,df4], axis=1)
#Unimos los dataframes para las ver los puntajes directos y porcentaje solamente
df6=pd.concat([df.iloc[:,1],df3,df4], axis=1)
#Guardamos en formato excel los dataframes unidos
#probablemente se necesitará la libreria openpyxl, podes instalar desde la terminal con la instrucción: pip install openpyxl
#Creamos el excel
df5.to_excel("Renzulli resultados.xlsx", sheet_name="Base de datos", index=False)
#Editamos el excel para agregar dos hojas al mismo archivo
writer = pd.ExcelWriter('Renzulli resultados.xlsx')
#La primera hoja contendrá todas las columnas
df5.to_excel(writer, sheet_name="Base de datos", index=False)
#La segunda hoja tendrá solamente los nombres, los puntajes directos y el porcentaje
#Al abrir el archivo excel probablemente te aparecerá un mensaje diciendo que intentará recuperar los datos, dale a aceptar y ya podrás ver
df6.to_excel(writer, sheet_name="Resultados", index=False)
writer.save()
writer.close()
