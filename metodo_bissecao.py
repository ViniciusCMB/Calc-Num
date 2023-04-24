import matplotlib.pyplot as plt
import numpy as np


def calcXn(k, l):
    return ((k+l)/(2))


def f(x, f):
    return eval(f, {"x": x})


def calcTol(i, j):
    return (abs(j - i))


def calcBiss(a, b, Tol):
    epsilon = 0
    x = 0
    iteration = 0
    xf = np.linspace(a-1, b+1, 100)
    yf = f(xf, function)

    a_zero = a
    b_zero = b

    epsilon = calcTol(a, b)

    while (epsilon > Tol):
        x = calcXn(a, b)

        f_A = f(a, function)
        f_B = f(b, function)
        f_x = f(x, function)

        if ((f_A)*(f_x) < 0):
            b = x
        elif ((f_B)*(f_x) < 0):
            a = x
        else:
            print("Error")
            break
        epsilon = calcTol(a, b)
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {epsilon} // {function} = {f(x, function):.4f} para x = {x:.4f}')
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
print('Cálculo Método da Bisseção')
print('===============')
function = input('Informe a função desejada: ')
limA = float(input('Indique o primeiro limitante do intervalo: '))
limB = float(input('Indique o segundo limitante do intervalo: '))
tol = float(input('Indique a tolerância: '))
calcBiss(limA, limB, tol)
