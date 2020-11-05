import matplotlib.pyplot as plt
import numpy as np


def plotting(abc):
    x = np.linspace(-20, 20, 1000)
    y = abc[0] * x**2 + abc[1] * x + abc[2]

    plt.plot(x, y)
    plt.grid()
    plt.show()


def plot(abc):
    plotting(abc)
