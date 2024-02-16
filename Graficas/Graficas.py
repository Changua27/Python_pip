import matplotlib.pyplot as plt

def Grafica_pie():
    nombres = ["A", "B", "C"]
    valores = [100, 200, 300]

    fig, ax= plt.subplots()
    ax.pie(valores, labels=nombres)
    plt.savefig("grafica.png")
    plt.close()