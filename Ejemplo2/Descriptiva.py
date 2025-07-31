import numpy as np
import pandas as pd
import argparse
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    parser = argparse.ArgumentParser(description="Análisis estadístico descriptivo")
    parser.add_argument( 
        "--seed",
        type=int,
        default=42,
        help="Establece la semilla para la generación de números aleatorios (default: 42)"
    )
    parser.add_argument( 
        "--imprimir_tendencia_central",
        action="store_true",
        help="Imprime las medidas de tendencia central"
    )
    parser.add_argument(
        "--imprimir_dispersion",
        action="store_true",
        help="Imprime las medidas de dispersión"
    )
    parser.add_argument(
        "--graficar_distribucion",
        action="store_true",
        help="Genera y muestra la gráfica de distribución de los datos"
    )

    args = parser.parse_args()

    if args.seed is not None:
        df = random_seed(args.seed)

    if args.imprimir_tendencia_central:
        imprimir_tendencia_central(df)

    if args.imprimir_dispersion:
        imprimir_dispersion(df)

    if args.graficar_distribucion:
        graficar_distribucion(df)
    

def random_seed(seed):
    np.random.seed(seed)
    print(f"Random seed set to: {seed}")
    datos = np.random.normal(loc=50, scale=10, size=100)
    df = pd.DataFrame(datos, columns=["Valores"])
    print(df.head())
    return df

def tendencia_central(df):
    media = df["Valores"].mean()
    mediana = df["Valores"].median()
    #moda = stats.mode(df["Valores"], keepdims=True)[0][0]
    moda = df.mode().iloc[0]["Valores"]
    # counts, bin_edges = np.histogram(df["Valores"], bins=15)
    # max_bin_index = np.argmax(counts)
    # moda = (bin_edges[max_bin_index] + bin_edges[max_bin_index + 1]) / 2
    return media, mediana, moda

def dispersion(df):
    rango = df["Valores"].max() - df["Valores"].min()
    varianza = df["Valores"].var()
    desviacion_std = df["Valores"].std()
    coef_variacion = (desviacion_std / df["Valores"].mean()) * 100
    return rango, varianza, desviacion_std, coef_variacion


def imprimir_tendencia_central(df):
    media, mediana, moda = tendencia_central(df)
    print("Medidas de tendencia central:")
    print(f"Media: {media:.2f}")
    print(f"Mediana: {mediana:.2f}")
    print(f"Moda: {moda:.2f}")

def imprimir_dispersion(df):
    rango, varianza, desviacion_std, coef_variacion = dispersion(df)
    print("\nMedidas de dispersión:")
    print(f"Rango: {rango:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación estándar: {desviacion_std:.2f}")
    print(f"Coeficiente de variación: {coef_variacion:.2f}%")

def graficar_distribucion(df): 
    media, mediana, moda = tendencia_central(df)
    rango, varianza, desviacion_std, coef_variacion = dispersion(df)
    plt.figure(figsize=(12, 6))
    sns.histplot(df["Valores"], bins=15, kde=True, color='skyblue')
    plt.axvline(media, color='red', linestyle='--', label=f"Media: {media:.2f}")
    plt.axvline(mediana, color='green', linestyle='--', label=f"Mediana: {mediana:.2f}")
    plt.axvline(moda, color='orange', linestyle='--', label=f"Moda: {moda:.2f}")
    plt.axvspan(media - desviacion_std, media + desviacion_std, color='red', alpha=0.1, label='±1 Desviación estándar')
    plt.text(media + desviacion_std + 1, plt.ylim()[1]*0.8, f"Desv. Estándar: {desviacion_std:.2f}", color='gray')
    plt.text(media + desviacion_std + 1, plt.ylim()[1]*0.7, f"Varianza: {varianza:.2f}", color='gray')
    plt.text(media + desviacion_std + 1, plt.ylim()[1]*0.6, f"Rango: {rango:.2f}", color='gray')
    plt.text(media + desviacion_std + 1, plt.ylim()[1]*0.5, f"Coef. Variación: {coef_variacion:.2f}%", color='gray')
    plt.title("Distribución de los datos con medidas de tendencia central")
    plt.xlabel("Valores")
    plt.ylabel("Frecuencia")
    plt.legend()
    plt.tight_layout()
    plt.savefig("Ejemplo2/estadistica_descriptiva.png")
    plt.show()

if __name__ == "__main__":
    main()
