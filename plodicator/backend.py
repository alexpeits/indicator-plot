import numpy as np
import matplotlib.pyplot as plt
try:
    import seaborn
except ImportError:
    pass
from sympy.abc import x as X
from sympy.core import sympify
from sympy.utilities.lambdify import lambdify
from sympy.printing.latex import latex


def plot(func_expr, left=0, right=100):
    func_sym = sympify(func_expr)
    title = latex(func_sym)
    func = lambdify(X, func_sym, 'numpy')
    x = np.linspace(left, right, 400)
    y = func(x)
    plt.plot(x, y)
    plt.title(r'${}$'.format(title), fontsize=18)
    plt.show()
