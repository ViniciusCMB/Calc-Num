import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator, MultipleLocator
import numpy as np

# Função que calcula f(x)
def f(x, f):
    return eval(f, {"x": x})

# Função que calcula a tolerância
def calcTol(i, j):
    return (abs(j - i))

# Função que calcula o método da Secante
def calcSec(a, b, Tol):
    fig = plt.figure()  
    fig.suptitle('Cálculo Método da Secante')
    ax = fig.add_subplot()
    eps = 0
    xold2 = 0.0
    xold = 0.0
    iteration = 0
    x_f = np.linspace(a-0.1, b+0.1, 100)
    y_f = f(x_f, function)

    a_zero = a
    b_zero = b

    eps = calcTol(a, b)

    while (eps > Tol):
        xold2 = b
        xold = a

        f_A = f(xold, function)
        f_B = f(xold2, function)

        x = xold - (f_A*((xold-xold2)/(f_A-f_B)))

        b = a
        a = x

        eps = calcTol(a, b)
        print(
            f'ITERAÇÃO {iteration} - Intervalo de soluções: [{a:.4f}, {b:.4f}] // Tol = {eps:.4f} // {function} = {f(x, function):.4f} para x = {x:.4f}')
        
        ax.scatter(b, f(b, function), c='red') # Exibe todos pontos/valores de aproximação em vermelho 
        iteration += 1

    ax.scatter(b, f(b, function), c='red', label=f'Xn')
    print(
        f'A solução mais próxima para {function} = 0, em [{a_zero:.4f}, {b_zero:.4f}] é x={x:.4f}')

    # Exibição do gráfico
    
    ax.grid()
    ax.set_title(f'{function}', loc='center', fontstyle='oblique', fontsize='medium')
    ax.scatter(a_zero, f(a_zero, function), c='blue', label='X0')
    ax.scatter(b_zero, f(b_zero, function), c='blue', label='X1')
    ax.scatter(a, f(a, function), c='orange', label='Raiz') # Exibe a raiz em laranja
    ax.annotate(f'Raiz em [{x:.4f}, {f(x, function):.4f}]', xy=(x, f(x, function)), xytext=(x, f(x, function)))
    ax.plot(x_f, y_f, c='purple', label='F(x)')
    y = np.zeros(100)
    ax.plot(x_f, y, c='gray', linestyle='dotted')
    ax.set_ylabel('F(x)')
    ax.set_xlabel('x')
    ax.legend()
    plt.show()
    return None


print('===============')
print('Cálculo Método da Secante')
print('===============')
function = input('Informe a função desejada: ')
limA = float(input('Indique o primeiro limitante do intervalo: '))
limB = float(input('Indique o segundo limitante do intervalo: '))
tol = float(input('Indique a tolerância: '))
calcSec(limA, limB, tol)
print('===============')