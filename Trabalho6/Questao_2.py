import numpy as np
import matplotlib.pyplot as plt

fig, ax= plt.subplots() 

def fat(n):
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1

    return fat

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

def calc_z(x, xi):
    h = xi[1]-xi[0]
    z = (x-xi[0])/h
    return z

def pol_Dif(x, dy): # Calcula o resultado do polinômio aplicado em x
    pontos = len(dy)
    z = calc_z(x, xi)
    s = 0
    for i in range(pontos):
        prod = 1
        for j in range(i):
                prod *= (z-j)
        prod *= dy[i]/fat(i)
        s += prod
    return s

xi = [136, 178, 220, 262]
yi = [15, 50, 66, 76]
x = 200

dy = calc_dy(xi, yi)

print('\nCalculadora Polinômio de Diferenças Finitas Ascendentes')

print('================================')
print(f'Xi = {xi}')
print(f'Yi = {yi}')
print('================================\n')

print(f'Dy: {dy}, z: {calc_z(x, xi):.4f}')
print(f'O resultado da interpolação no ponto x = {x}, é {pol_Dif(x, dy):.4f}')

ax.grid()
ax.scatter(x, pol_Dif(x, dy), c='green', label=f'P={x}')
ax.scatter(xi, yi, c='red', label='Pontos')
ax.set_title("Gráfico Solubilidade x Temperatura")

p = np.linspace(min(xi), max(xi), 100)
px = [pol_Dif(xn, dy) for xn in p]

ax.plot(p, px, c='purple', label='P(x)')
ax.set_ylabel('Temperatura (°C)')
ax.set_xlabel('Solubilidade (ppm)')
ax.legend()

plt.show()