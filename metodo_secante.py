import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve


def f(x):
    return ((x**5) - (2*(x)) - 1)


def calcTol(i, j):
    return (abs(j - i))


def calcSec(a, b, Tol):
    epsilon = 0
    xtemp = 0.0
    xold = 0.0
    iteration = 0
    xf = np.linspace(a-1, b+1, 100)
    yf = xf**5 - 2*xf - 1

    a_zero = a
    b_zero = b

    epsilon = calcTol(a, b)

    while (epsilon > Tol):
        xtemp = b
        xold = a

        f_A = f(xold)
        f_B = f(xtemp)

        x = xold - (f_A*((xold-xtemp)/(f_A-f_B)))

        b = a
        a = x

        epsilon = calcTol(a, b)
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {epsilon:.4f} // {function} = {f(x):.4f} para x = {x:.4f}')
        iteration += 1

    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] é x={x:.4f}')
    plt.grid()
    plt.title(f'{function}')
    plt.scatter(a, f(a), c='blue')
    plt.scatter(b, f(b), c='blue')
    plt.scatter(a_zero, f(a_zero), c='red')
    plt.scatter(b_zero, f(b_zero), c='red')
    plt.plot(xf, yf, c='purple')
    plt.show()
    return None


function = "x^5 - 2x - 1"
print(f'Cálculo Método da Secante para a função "{function}"')
limA = float(input("Indique o primeiro limitante do intervalo: "))
limB = float(input("Indique o segundo limitante do intervalo: "))
tol = float(input("Indique a tolerância: "))
calcSec(limA, limB, tol)
