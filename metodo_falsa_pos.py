import matplotlib.pyplot as plt
import numpy as np

# Função que calcula Xn
def calcXn(k, l):
    return ((k*f(l, function)-l*f(k, function))/(f(l, function)-f(k, function)))

# Função que calcula f(x)
def f(x, f):
    return eval(f, {"x": x})

# Função que calcula a tolerância
def calcTol(i):
    return (abs(i))

# Função que calcula o método da Falsa Posição
def calcFals(a, b, Tol):
    epsilon = 0
    x = 0
    iteration = 0
    xf = np.linspace(a-1, b+1, 100)
    yf = f(xf, function)

    a_zero = a
    b_zero = b

    x = calcXn(a, b)

    epsilon = calcTol(f(x, function))

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
        epsilon = calcTol(f(x, function))
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {epsilon:.4f} // {function} = {f(x, function):.4f} para x = {x:.4f}')
        iteration += 1

    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] e tolerância de {Tol} é x={x:.4f}')

    # Exibição do gráfico
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
print('Cálculo Método da Falsa Posição')
print('===============')
function = input('Informe a função desejada: ')
limA = float(input('Indique o primeiro limitante do intervalo: '))
limB = float(input('Indique o segundo limitante do intervalo: '))
tol = float(input('Indique a tolerância: '))
calcFals(limA, limB, tol)
print('===============')