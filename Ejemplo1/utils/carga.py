import pandas as pd

# dataframe de pandas: el datafram es una estructura de datos bidimensional, 
# similar a una tabla en una base de datos o una hoja de cálculo de Excel.
def cargar_datos(ruta_csv):
    return pd.read_csv(ruta_csv, sep=",", encoding="utf-8")



