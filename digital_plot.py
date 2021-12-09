import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
from numpy.lib.function_base import append

def char_to_bin(data: str):
    assert (len(data) == 1), 'Impossible to convert data'
    bits = []
    bin = ord(data)
    for i in range(7, -1, -1):
        bits.append((bin & (1 << i)) >> i)
    return bits

def plot_nrz_l(data: str):
    bits = char_to_bin(data)
    data_plt = np.append(np.repeat(bits, 2), bits[-1])
    t = 0.5 * np.arange(len(data_plt))
    plt.step(t, data_plt, 'r', linewidth = 2, where='post')
    plt.ylim([-0.5, 2])
    plt.xlim([0, 8])
    for tbit, bit in enumerate(bits):
        plt.text(tbit + 0.5, 1.1, str(bit))
    plt.gca().grid(axis='x')
    plt.gca().set_yticks([0, 1])
    plt.show()

def plot_manchester_IEEE(data: str):
    bits = char_to_bin(data)
    data_plt = np.append(np.repeat(bits, 2), not bits[-1])
    clock = np.arange(len(data_plt)) % 2
    manchester = 1 - np.logical_xor(clock, data_plt)
    manchester = np.where(manchester == 0, -1, manchester)
    t = 0.5 * np.arange(len(data_plt))
    plt.step(t, manchester, 'r', linewidth = 2, where='post')
    plt.ylim([-1.5, 1.5])
    plt.xlim([0, 8])
    for tbit, bit in enumerate(bits):
        plt.text(tbit + 0.5, 1.1, str(bit))
    plt.gca().grid(axis='x')
    plt.gca().set_yticks([-1, 0, 1])
    plt.show()

def plot_PAM4(data: str):
    bits = char_to_bin(data)
    sym = []
    for i in range(0, len(bits), 2):
        if bits[i] == 0 and bits[i+1] == 0:
            sym.append(-2)
        elif bits[i] == 0 and bits[i+1] == 1:
            sym.append(-1)
        elif bits[i] == 1 and bits[i+1] == 0:
            sym.append(2)
        else:
            sym.append(1)
    data_plt = np.append(np.repeat(sym, 2), sym[-1])
    t = 0.5 * np.arange(len(data_plt))
    plt.step(t, data_plt, 'r', linewidth = 2, where='post')
    plt.ylim([-2.5, 2.5])
    plt.xlim([0, 4])
    for tbit, bit in enumerate(bits):
        plt.text(tbit/2 + 0.2, 1.1, str(bit))
    plt.gca().grid(axis='x')
    plt.gca().set_yticks([-2, -1, 0, 1, 2])
    plt.show()

def plot_ask(data: str, freq: float):
    bits = char_to_bin(data)
    x = np.arange(0, len(bits), 0.01)
    A = []
    for i in range(0, len(x)):
        A.append(2 if bits[i//100] == 1 else 0.5)
    y = A*np.sin(freq*np.pi*x)
    plt.ylim([-2.1, 3])
    plt.plot(x, y)
    for tbit, bit in enumerate(bits):
        plt.text(tbit + 0.5, 2.1, str(bit))
    plt.gca().grid(axis='x')
    plt.gca().set_yticks([-2, -0.5, 0, 0.5, 2])
    plt.show()

