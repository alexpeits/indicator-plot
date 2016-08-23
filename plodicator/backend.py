import numpy as np
import matplotlib.pyplot as plt


def plot(func, left=0, right=100):
    func = func.replace('^', '**')
    func = func.replace('sin', 'np.sin')
    func = func.replace('cos', 'np.cos')
    func = func.replace('pi', 'np.pi')
    func = func.replace('sqrt', 'np.sqrt')
    x = np.linspace(left, right, 400)
    y = eval(func)
    plt.plot(x, y)
    plt.show()
