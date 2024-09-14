# Método de lagrange
import numpy as np
import matplotlib.pyplot as plt
from sympy import *

fig, (ax1, ax2) = plt.subplots(2, sharex=True) # Cria a figura para o gráfico, sendo dois gráficos que compartilham o eixo x
init_printing(pretty_print=True)
z = Symbol('Z')
x0 = Symbol('X0')
h = Symbol('h')
ln = Symbol('Ln')
l0 = Symbol('L0')
l1 = Symbol('L1')
l2 = Symbol('L2')
P = symbols('P', cls = Function)

xi = [2.5 , 3, 3.5]
yi = [0.503, 0.0806, 1.192]
x = 2.8

def coef_lagrange(x, y): # Calcula os coeficientes do polinômio
    pontos = len(x)
    coef = []
    for i in range(pontos):
        prod = 1
        for j in range(pontos):
            if i!= j:
                prod *= (x[i]-x[j])
        ci = (y[i]/prod)
        coef.append(ci)
    return coef

def pol_lagrange(x, xn, coef): # Calcula o resultado do polinômio aplicado em x
    s = 0
    num = len(coef)
    for i in range(num):
        prod = 1
        for j in range(num):
            if i!= j:
                prod *= (x-xn[j])
        prod *= coef[i]
        s += prod
    return s

def lagrange(): # Calcula a posição no instante t = 10, imprime o resultado e gera o gráfico
    coef_lgr = coef_lagrange(xi, yi)
    print(f'B) Dado o polinômio:\n')
    px = l0*yi[0]+l1*yi[1]+l2*yi[2]
    pprint(px)
    print(f'\nTal que:\n')
    pprint(Eq(coef_lgr[0], l0))
    pprint(Eq(coef_lgr[1], l1))
    pprint(Eq(coef_lgr[2], l2))
    print(f'\nO valor aproximado pelo Polinômio de Lagrange para x={x} é {pol_lagrange(x, xi, coef_lgr)}')
    ax2.grid()
    ax2.scatter(x, pol_lagrange(x, xi, coef_lgr), c='green', label=f'X={x}')
    ax2.text(x, 0.4, rf'${latex(P(x))}$'+f'={pol_lagrange(x, xi, coef_lgr):.4f}',
        horizontalalignment='center', fontsize=15, c='green')
    ax2.scatter(xi, yi, c='blue', label='Pontos')
    ax2.set_title("Gráfico Xi x Yi - (B)")
    p = np.linspace(min(xi), max(xi), 100)
    px = [pol_lagrange(i, xi, coef_lgr) for i in p]
    ax2.plot(p, px, c='purple', label='P(x)')
    ax2.set_ylabel('Y')
    ax2.set_xlabel('X')
    ax2.legend()

def calc_dy(x, y): # Calcula o delta y
    pontos = len(x)
    Y = [item for item in y]
    dy = np.zeros(pontos)
    dy[0] = y[0]
    for i in range(pontos-1):
        for j in range(pontos-1-i): 
            y0 = Y[j+1] - Y[j]
            Y[j]= y0
        dy[i+1] = Y[0]
    return dy

def fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat

def calc_z(x, xi):
    h = xi[1]-xi[0]
    z = (x-xi[0])/h
    return z

def diff_newton(): # Calcula a velocidade no instante t = 10, imprime o resultado e gera o gráfico

    dy = calc_dy(xi, yi)
    pol = dy[0]+((z/fat(1))*dy[1])+(((z*(z-1))/fat(2))*dy[2])
    print(f'A) Dado o polinômio:\n')
    pprint(expand(pol))
    print(f'\nOnde Z é definido por:\n')
    pprint(Eq((x-x0)/h, z))
    
    print(f'\nO valor aproximado pelo Polinômio da Derivação Numérica para x={x} é {pol.subs(z, (calc_z(x, xi)))}')
    print(f'\n==================================\n')

    ax1.grid()
    ax1.scatter(x, pol.subs(z, (calc_z(x, xi))), c='green', label=f'X={x}')
    ax1.scatter(xi, yi, c='red', label='Pontos')
    ax1.set_title("Gráfico Xi x Yi - (A)")
    p = np.linspace(min(xi), max(xi), 100)
    px = [pol.subs(z, (calc_z(i, xi))) for i in p]
    ax1.plot(p, px, c='purple', label='P(x)')
    ax1.set_ylabel('Y')
    ax1.text(x, 0.4, rf'${latex(P(x))}$'+f'={pol.subs(z, (calc_z(x, xi))):.4f}',
        horizontalalignment='center', fontsize=15, c='green')
    ax1.legend()


print(f'\n==================================\n')
print(f'Calculadora para valor aproximado pelo Polinômio da Derivação Numérica(A) e Lagrange(B) para x={x} dados os pontos Xi={xi} e Yi={yi}\n')
diff_newton()
lagrange()
print(f'\n==================================\n')
plt.show()