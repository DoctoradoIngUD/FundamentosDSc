import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt
import argparse

def main():
    parser = argparse.ArgumentParser(description="Análisis estadístico inferencial")
    parser.add_argument(
        "--seed",
        type=int,
        default=42,
        help="Establece la semilla para la generación de números aleatorios (default: 42)"
    )
    parser.add_argument( "--muestra",
        action="store_true",
        help="Genera una muestra aleatoria de la población"
    )
    parser.add_argument( "--parametros_estadisticos",
        action="store_true",
        help="Calcula y muestra los parámetros estadísticos de la población y la muestra"
    )
    parser.add_argument( "--intervalo_confianza",
        action="store_true",
        help="Calcula el intervalo de confianza al 95% para la media muestral"
    )
    parser.add_argument( "--contraste_hipotesis",
        nargs="?",
        const=52,
        type=float,
        default=None,
        help="Realiza un contraste de hipótesis para la media poblacional (default: 52)"
    ) 
    parser.add_argument( "--visualizacion",
        action="store_true",
        help="Genera una visualización de la distribución de la población y la muestra"
    )
    parser.add_argument( "--error_muestreo",
        action="store_true",
        help="Calcula el error de muestreo entre la media poblacional y la media muestral"
    )
    parser.add_argument( "--print_results",
        action="store_true",
        help="Imprime los resultados del análisis de estadística inferencial"
    )

    args = parser.parse_args()

    if args.seed is not None:
        poblacion = random_seed(args.seed)
    else:
        poblacion = random_seed(42)  # Valor por defecto

    if args.muestra:
        muestra(poblacion)
        return

    if args.parametros_estadisticos:
        Mst = muestra(poblacion)
        parametros_estadisticos(poblacion, Mst)
        return

    if args.intervalo_confianza:
        Mst = muestra(poblacion)
        media_poblacional, media_muestral, desviacion_muestral = parametros_estadisticos(poblacion, Mst)
        estimacion_intervalo_confianza(media_muestral, desviacion_muestral, Mst)
        return

    if args.contraste_hipotesis is not None:
        Mst = muestra(poblacion)
        contraste_hipotesis(Mst, args.contraste_hipotesis)
    else:
        Mst = muestra(poblacion)
        contraste_hipotesis(Mst, 52)  

    if args.visualizacion:
        Mst = muestra(poblacion)
        media_poblacional, media_muestral, _ = parametros_estadisticos(poblacion, Mst)
        visualizacion(poblacion, Mst, media_poblacional, media_muestral)
        return

    if args.error_muestreo:
        Mst = muestra(poblacion)
        media_poblacional, media_muestral, _ = parametros_estadisticos(poblacion, Mst)
        error_muestreo(media_poblacional, media_muestral)
        return

    if args.print_results:
        Mst = muestra(poblacion)
        media_poblacional, media_muestral, desviacion_muestral = parametros_estadisticos(poblacion, Mst)
        intervalo = estimacion_intervalo_confianza(media_muestral, desviacion_muestral, Mst)
        t_stat, p_valor = contraste_hipotesis(Mst, 52)
        error_muestreo_value = error_muestreo(media_poblacional, media_muestral)
        print_results(media_poblacional, media_muestral, intervalo, t_stat, p_valor, error_muestreo_value)
        return


def random_seed(seed):
    np.random.seed(seed)
    print(f"Semilla aleatoria establecida: {seed}")
    poblacion = np.random.normal(loc=50, scale=10, size=10000)  # media=50, desviación=10
    return poblacion


def muestra(poblacion):
    muestra = np.random.choice(poblacion, size=100, replace=False)
    print(f"Muestra generada de tamaño {len(muestra)}")
    print(f"Primeros 5 valores de la muestra: {muestra[:5]}")
    return muestra


def parametros_estadisticos(poblacion, muestra):
    media_poblacional = np.mean(poblacion)
    media_muestral = np.mean(muestra)
    desviacion_muestral = np.std(muestra, ddof=1)  # ddof=1 para obtener la desviación estándar muestral
    print(f"Resultado de los parametros estdisticos: \n media pob:  {media_poblacional} \n media muestral: {media_muestral} \n desviación muestral: {desviacion_muestral}")
    return media_poblacional, media_muestral, desviacion_muestral

def estimacion_intervalo_confianza(media_muestral, desviacion_muestral, muestra):
    nivel_confianza = 0.95
    error_estandar = desviacion_muestral / np.sqrt(len(muestra))
    intervalo = stats.t.interval(nivel_confianza, df=len(muestra)-1, loc=media_muestral, scale=error_estandar)
    print(f"Intervalo de confianza al {nivel_confianza*100}%: [{intervalo[0]:2f},  {intervalo[1]:.2f}]") 
    return intervalo

def contraste_hipotesis(muestra, mu_hipotetico):
    t_stat, p_valor = stats.ttest_1samp(muestra, mu_hipotetico)
    print(f"Contraste de hipótesis: H₀: μ = {mu_hipotetico}")
    print(f"Estadístico t: {t_stat:.3f}, Valor p: {p_valor:.3f}")
    return t_stat, p_valor

def error_muestreo(media_poblacional, media_muestral):
    error_muestreo = abs(media_poblacional - media_muestral)
    print(f"Error de muestreo: {error_muestreo:.2f}")
    return error_muestreo

def visualizacion(poblacion, muestra, media_poblacional, media_muestral):
    plt.figure(figsize=(10, 6))
    plt.hist(poblacion, bins=50, alpha=0.5, label='Población')
    plt.hist(muestra, bins=30, alpha=0.7, label='Muestra')
    plt.axvline(media_poblacional, color='blue', linestyle='dashed', linewidth=2, label=f'Media poblacional: {media_poblacional:.2f}')
    plt.axvline(media_muestral, color='red', linestyle='dashed', linewidth=2, label=f'Media muestral: {media_muestral:.2f}')
    plt.title('Distribución de la población y la muestra')
    plt.xlabel('Valor')
    plt.ylabel('Frecuencia')
    plt.legend()
    plt.tight_layout()
    plt.show()

def print_results(media_poblacional, media_muestral, intervalo, t_stat, p_valor, error_muestreo):
    print("📊 Resultados del análisis de estadística inferencial")
    print(f"1. Media poblacional: {media_poblacional:.2f}")
    print(f"2. Media muestral: {media_muestral:.2f}")
    print(f"3. Estimación puntual: {media_muestral:.2f}")
    print(f"4. Intervalo de confianza al 95%: [{intervalo[0]:.2f}, {intervalo[1]:.2f}]")
    print("5. Contraste de hipótesis (H₀: μ = 52):")
    print(f"   - Estadístico t: {t_stat:.3f}")
    print(f"   - Valor p: {p_valor:.3f}")
    print("   - " + ("No se rechaza H₀ al 5% de significancia" if p_valor > 0.05 else "Se rechaza H₀ al 5% de significancia"))
    print(f"6. Error de muestreo: {error_muestreo:.2f}")
    print("7. Nivel de confianza: 95%")

if __name__ == "__main__":
    main()
