import seaborn as sns
import matplotlib.pyplot as plt

def grafico_supervivencia(df):
    """Gráfico de conteo de supervivencia."""
    sns.countplot(data=df, x="Survived")
    plt.title("Distribución de Supervivencia")
    plt.xlabel("Survived (0 = No, 1 = Sí)")
    plt.ylabel("Cantidad")
    plt.show()

def grafico_edad_por_sexo(df):
    """Histograma de edad por sexo."""
    sns.histplot(data=df, x="Age", hue="Sex", multiple="stack", bins=20)
    plt.title("Distribución de Edad por Sexo")
    plt.xlabel("Edad")
    plt.ylabel("Frecuencia")
    plt.show()

def grafico_tarifa_por_clase(df):
    """Boxplot de tarifas por clase."""
    sns.boxplot(data=df, x="Pclass", y="Fare")
    plt.title("Distribución de Tarifas por Clase")
    plt.xlabel("Clase")
    plt.ylabel("Tarifa")
    plt.show()
