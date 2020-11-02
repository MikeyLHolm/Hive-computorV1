import matplotlib.pyplot as plt
import numpy as np


def plotting(abc):
    # create 1000 equally spaced points between -20 and 20
    x = np.linspace(-20, 20, 1000)

    # calculate the y value for each element of the x vector
    y = abc[0] * x**2 + abc[1] * x + abc[2]

    plt.plot(x, y)
    plt.grid()
    plt.show()


def plot(abc):
    plotting(abc)
