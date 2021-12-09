import numpy as np
import matplotlib.pyplot as plt
import sys

def config_axis(fig):
    """Sets the default axis condiguration"""
    ax = fig.add_subplot(1, 1, 1)
    ax.set_xlabel('tiempo')
    ax.set_ylabel('amplitud')

def main():
    # filename = input('Nombre del archivo de salida')
    # Cambia estos valores indicando las posiciones de los unos
    data = [1, 1, 1, 0, 0, 1, 0]
    t = np.arange(0,data[-1]+3)
    x = np.zeros_like(t)
    x[data] = 1
    fig = plt.figure()
    config_axis(fig)
    plt.step(t, x, where="post", color='steelblue')
    plt.show()
    # plt.savefig(filename, dpi=300)

if __name__ == "__main__":
    main()