import os #librería para interactuar con el sistema operativo
import argparse #librería para manejar argumentos de línea de comandos
from utils.carga import cargar_datos
from utils.mostrar import (
    mostrarColumnas as mostrar_columnas,
    mostrarCabecera as mostrar_cabecera,
    mostrarCabeceraN,
    mostrarCola as mostrar_cola,
    mostrarColaN,
    mostrar_info,
    estadistica_descriptiva,
)
from utils.visualizaciones import (
    grafico_supervivencia,
    grafico_edad_por_sexo,
    grafico_tarifa_por_clase,
)

def main():
    parser = argparse.ArgumentParser(description="Análisis del dataset del Titanic")
    parser.add_argument(
        "--mostrar_columnas", 
        action="store_true",  # Indica que este argumento es un flag, no requiere valo
        help="Muestra las columnas del DataFrame"
    )
    parser.add_argument(
        "--mostrar_cabecera", action="store_true", help="Muestra los primeros registros del DataFrame"
    )
    parser.add_argument(
        "--mostrar_cabecera_n",
        type=int, #indica que este argumento espera un entero
        help="Muestra los primeros n registros del DataFrame"
    )
    parser.add_argument(
        "--mostrar_cola", action="store_true", help="Muestra los últimos registros del DataFrame"
    )
    parser.add_argument(
        "--mostrar_cola_n",
        type=int,
        help="Muestra los últimos n registros del DataFrame"
    )
    parser.add_argument(
        "--mostrar_info", action="store_true", help="Muestra información general del DataFrame"
    )
    parser.add_argument(
        "--estadistica_descriptiva",
        action="store_true",
        help="Muestra estadísticas descriptivas del DataFrame"
    )
    parser.add_argument(
        "--visualizar_supervivencia",
        action="store_true",
        help="Visualiza el gráfico de supervivencia"
    )
    parser.add_argument(
        "--visualizar_edad_por_sexo",
        action="store_true",
        help="Visualiza el histograma de edad por sexo"
    )
    parser.add_argument(
        "--visualizar_tarifa_por_clase",
        action="store_true",
        help="Visualiza el boxplot de tarifas por clase"
    )
    args = parser.parse_args() # Analiza los argumentos de la línea de comandos
    ruta = "Ejemplo1/data/titanic.csv"
    if not os.path.exists(ruta):
        print(f"⚠️  Error: El archivo '{ruta}' no fue encontrado. Verifica la ruta o asegúrate de que el archivo exista.")
        return
    df = cargar_datos(ruta)

    if args.mostrar_columnas:
        mostrar_columnas(df)

    if args.mostrar_cabecera:
        mostrar_cabecera(df)

    if args.mostrar_cabecera_n is not None:
        mostrarCabeceraN(df, args.mostrar_cabecera_n)

    if args.mostrar_cola:
        mostrar_cola(df)

    if args.mostrar_cola_n is not None:
        mostrarColaN(df, args.mostrar_cola_n)

    if args.mostrar_info:
        mostrar_info(df)

    if args.estadistica_descriptiva:
        estadistica_descriptiva(df)
  
    if args.visualizar_supervivencia:
        grafico_supervivencia(df)   

    if args.visualizar_edad_por_sexo:
        grafico_edad_por_sexo(df)

    if args.visualizar_tarifa_por_clase:
        grafico_tarifa_por_clase(df)
    


if __name__ == "__main__": # Es el piunto de entrada del programa
    main() #Es la función principal que se ejecuta al iniciar el programa
