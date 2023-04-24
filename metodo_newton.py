import matplotlib.pyplot as plt
import numpy as np
from sympy import diff, Symbol


def f(x, f):
    return eval(f, {"x": x})


def dxf(f):
    x = Symbol('x')
    return str(diff(eval(f), x))


def calcTol(i, j):
    return (abs(j - i))


def calcNR(a, b, Tol):
    epsilon = 0
    xold = 0.0
    iteration = 0
    xf = np.linspace(a-1, b+1, 100)
    yf = f(xf, function)

    a_zero = a
    b_zero = b

    epsilon = calcTol(a, b)

    while (epsilon > Tol):
        xold = a

        f_A = f(xold, function)
        dxf_A = f(xold, dxf(function))

        x = xold - (f_A/dxf_A)

        b = a
        a = x

        epsilon = calcTol(a, b)
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {epsilon:.4f} // {function} = {f(x, function):.4f} para x = {x:.4f}')
        iteration += 1

    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] é x={x:.4f}')
    plt.grid()
    plt.title(f'{function}')
    plt.scatter(a, f(a, function), c='blue')
    plt.scatter(b, f(b, function), c='blue')
    plt.scatter(a_zero, f(a_zero, function), c='red')
    plt.scatter(b_zero, f(b_zero, function), c='red')
    plt.plot(xf, yf, c='purple')
    plt.show()
    return None


print('===============')
print('Cálculo Método de Newton Raphson')
print('===============')
function = input('Informe a função desejada: ')
limA = float(input('Indique o primeiro limitante do intervalo: '))
limB = float(input('Indique o segundo limitante do intervalo: '))
tol = float(input('Indique a tolerância: '))
calcNR(limA, limB, tol)
