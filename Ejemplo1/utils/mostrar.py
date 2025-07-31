def mostrarColumnas(df): #muestra las columnas del DataFrame
    print( df.columns )

def mostrarCabecera(df): #muestra los primeros registros del DataFrame
    print( df.head() )

def mostrarCabeceraN(df, n): #muestra los primeros n registros del DataFrame
    print(df.head(n))

def mostrarCola(df): #muestra los ultimos registros del DataFrame
    print(df.tail())

def mostrarColaN(df, n): #muestra los ultimos n registros del DataFrame
    print(df.tail(n))

def mostrar_info(df): # Muestra información general del DataFrame
    print("Información del DataFrame:")
    print(df.info())

def estadistica_descriptiva(df): # Muestra estadísticas descriptivas del DataFrame
    print("Estadísticas descriptivas del DataFrame:")
    print(df.describe(include='all'))
    
