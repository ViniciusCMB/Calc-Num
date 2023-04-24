import matplotlib.pyplot as plt
import numpy as np


def calcXn(k, l):
    return ((k*f(l)-l*f(k))/(f(l)-f(k)))


def f(x):
    return eval(function, {"x": x})


def calcTol(i):
    return (abs(i))


def calcFals(a, b, Tol):
    epsilon = 0
    x = 0
    iteration = 0
    xf = np.linspace(a-1, b+1, 100)
    yf = f(xf)

    a_zero = a
    b_zero = b

    x = calcXn(a, b)
    f_x = f(x)

    epsilon = calcTol(f(x))

    while (epsilon > Tol):
        x = calcXn(a, b)

        f_A = f(a)
        f_B = f(b)
        f_x = f(x)

        if ((f_A)*(f_x) < 0):
            b = x
        elif ((f_B)*(f_x) < 0):
            a = x
        else:
            print("Error")
            break
        epsilon = calcTol(f(x))
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {epsilon:.4f} // {function} = {f(x):.4f} para x = {x:.4f}')
        iteration += 1

    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] e tolerância de {Tol} é x={x:.4f}')

    plt.grid()
    plt.title(f'{function}')
    plt.scatter(a, f(a), c='blue')
    plt.scatter(b, f(b), c='blue')
    plt.scatter(a_zero, f(a_zero), c='red')
    plt.scatter(b_zero, f(b_zero), c='red')
    plt.plot(xf, yf, c='purple')
    plt.show()
    return None


print('===============')
print('Cálculo Método da Falsa Posição')
print('===============')
function = input('Informe a função desejada: ')
limA = float(input('Indique o primeiro limitante do intervalo: '))
limB = float(input('Indique o segundo limitante do intervalo: '))
tol = float(input('Indique a tolerância: '))
calcFals(limA, limB, tol)
