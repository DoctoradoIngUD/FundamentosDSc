import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, binom, expon, poisson

import argparse

#Alturas humanas estandarizadas o errores comunes de medición
def normal_distribution(mu=0, sigma=1): #mu es la media de el conjunto de datos y sigma es la desviación estándar
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    y = norm.pdf(x, mu, sigma)
    plt.figure(figsize=(12, 6))
    plt.title(f'Distribución Normal (μ={mu}, σ={sigma})')
    plt.axvline(mu, color='red', linestyle='--', label='Media: {:.2f}'.format(mu))
    plt.tight_layout()
    plt.plot(x, y, label='Altura', color='blue')
    plt.grid(True)
    plt.legend()
    plt.show()
#Lanzar una moneda n veces y contar caras
def binomial_distribution(n=10, p=0.5): #n es el numero de lazamientos de moneda y p es probabilidad de obtener cara
    x = np.arange(0, n+1)
    y = binom.pmf(x, n, p)
    plt.stem(x, y, basefmt=" ")
    plt.title(f'Distribución Binomial (n={n}, p={p})')
    plt.grid(True)
    plt.show()
#Tiempo entre llamadas en un call center
def exponencial_distribution(lamb=1.5): #lamb es la tasa de ocurrencia de llamdas por unidad de tiempo
    x = np.linspace(0, 5, 1000)
    y = expon.pdf(x, scale=1/lamb)
    plt.plot(x, y)
    plt.title(f'Distribución Exponencial (λ={lamb})')
    plt.grid(True)
    plt.show()
#Número de autos que pasan por un punto de control por unidad de tiempo min o hora
def poisson_distribution(lamb=3): #lamb es la tasa promedio de que un auto pase por el punto de control por unidad de tiempo
    x = np.arange(0, 15)
    y = poisson.pmf(x, lamb)
    plt.stem(x, y, basefmt=" ")
    plt.title(f'Distribución de Poisson (λ={lamb})')
    plt.grid(True)
    plt.show()

def main():
    parser = argparse.ArgumentParser(description="Visualización de distribuciones")
    subparsers = parser.add_subparsers(dest="dist")

    # Normal
    parser_normal = subparsers.add_parser("normal")
    parser_normal.add_argument("--mu", type=float, default=0)
    parser_normal.add_argument("--sigma", type=float, default=1)

    # Binomial
    parser_binomial = subparsers.add_parser("binomial")
    parser_binomial.add_argument("--n", type=int, default=10)
    parser_binomial.add_argument("--p", type=float, default=0.5)

    # Exponencial
    parser_exponencial = subparsers.add_parser("exponencial")
    parser_exponencial.add_argument("--lambdae", type=float, default=1.5)

    # Poisson
    parser_poisson = subparsers.add_parser("poisson")
    parser_poisson.add_argument("--lambdap", type=float, default=3)

    args = parser.parse_args()

    if args.dist == "normal":
        normal_distribution(args.mu, args.sigma)
    elif args.dist == "binomial":
        binomial_distribution(args.n, args.p)
    elif args.dist == "exponencial":
        exponencial_distribution(args.lambdae)
    elif args.dist == "poisson":
        poisson_distribution(args.lambdap)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
