import matplotlib.pyplot as plt
import numpy as np

# Função que calcula Xn
def calcXn(a, b):
    return ((a+b)/(2))

# Função que calcula f(x)
def f(x, f):
    return eval(f, {"x": x})

# Função que calcula a tolerância
def calcTol(i, j):
    return (abs(j - i))

# Função que calcula o método da Bisseção
def calcBiss(a, b, Tol):
    fig = plt.figure()  # an empty figure with no Axes
    fig.suptitle('Cálculo Método da Bisseção')
    ax = fig.add_subplot()

    eps = 0
    x = 0
    iteration = 0
    x_f = np.linspace(a-1, b+1, 100)
    y_f = f(x_f, function)

    a_zero = a
    b_zero = b

    eps = calcTol(a, b)

    while (eps > Tol):
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

        plt.scatter(x, f(x, function), c='red')

        eps = calcTol(a, b)
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {eps} // {function} = {f(x, function):.4f} para x = {x:.4f}')
        iteration += 1

    plt.scatter(x, f(x, function), c='red', label='Xn')

    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] é x={x:.4f}')

    # Exibição do gráfico
    ax.grid()
    ax.set_title(f'{function}', loc='center', fontstyle='oblique', fontsize='medium')
    ax.scatter(a_zero, f(a_zero, function), c='blue', label='X0')
    ax.scatter(b_zero, f(b_zero, function), c='blue', label='X1')
    ax.scatter(x, f(x, function), c='orange', label='Raiz') # Exibe a raiz em laranja
    ax.annotate(f'Raiz em em [{x:.4f}, {f(x, function):.4f}]', xy=(x, f(x, function)), xytext=(x, f(x, function)))
    ax.plot(x_f, y_f, c='purple', label='F(x)')
    y = np.zeros(100)
    ax.plot(x_f, y, c='gray', linestyle='dotted')
    ax.set_ylabel('F(x)')
    ax.set_xlabel('x')
    ax.legend()
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
print('===============')
