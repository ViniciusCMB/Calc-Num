from sympy import *
import numpy as np
import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(2) # Cria a figura para o gráfico, sendo dois gráficos


init_printing(pretty_print=True)
z = Symbol('z')
p = symbols('P', cls = Function)

def tempo(t):
  hora, minutostr = str(t).split('.')

  minuto = int(int(minutostr)*0.6)
  horario = hora +":"+ str(minuto)
  return horario

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

xa = [5, 6, 7, 8]
ya = [16.4, 15.2, 14.9, 16]

dya = calc_dy(xa, ya)

eq1 = dya[0]+((z/fat(1))*dya[1])+(((z*(z-1))/fat(2))*dya[2])+(((z*(z-1)*(z-2))/fat(3))*dya[3])

print(f'\n==================================\n')

print(f'Para analisar o consumo máximo e mínimo no intervalo Xi[{xa[0]},{xa[3]}]\n')

print(f'Dada a equação do polinômio: ')
pprint(Eq(eq1, p(5+z)))

print(f'\nCom o objetivo de achar o menor consumo no intervalo de pontos:\n')

derivada1a = solve(Eq(diff(eq1, z, 1), 0), z)
print(f'Aplicando 0 na derivada primeira de {p(5+z)}, as raízes são: {derivada1a}')

derivada2a = [0,0]
derivada2a[0] = diff(eq1, z, 2).subs(z, (derivada1a[0]))
derivada2a[1] = diff(eq1, z, 2).subs(z, (derivada1a[1]))
print(f'Aplicando os pontos {derivada1a} na derivada segunda de {p(13+z)} temos: {derivada2a}')

consumo = [0,0,0,0]
consumo[0] = eq1.subs(z, (derivada1a[0]))
consumo[1] = eq1.subs(z, (derivada1a[1]))
print(f'\nPortando, dado os pontos de maior e menor consumo em {p((5+derivada1a[0]))} com z={derivada1a[0]} e {p((5+derivada1a[1]))} com z={derivada1a[1]}\nO consumo estimado foi: máx = {consumo[0]}MW e min: {consumo[1]}MW')

ax1.grid()
ax1.scatter((5+derivada1a[0]), consumo[0], c='green', label='Máx')
ax1.scatter((5+derivada1a[1]), consumo[1], c='green', label='Min')
ax1.scatter(xa, ya, c='red', label='Pontos')
ax1.set_title("Gráfico Consumo x Tempo")
x2a = [5, 6, 7, 8, 1.6361]
a = np.linspace(min(x2a), max(x2a), 100)
ax = [eq1.subs(z, (xi-x2a[0])) for xi in a]
ax1.plot(a, ax, c='purple', label='P(x)')
ax1.set_ylabel('Consumo (MW)')
ax1.set_xlabel('Tempo (h)')
ax1.legend()

print(f'\n==================================\n')
xb = [13, 14, 15, 16]
yb = [36.5, 43, 34, 31.2]
dyb = calc_dy(xb, yb)

eq2 = dyb[0]+((z/fat(1))*dyb[1])+(((z*(z-1))/fat(2))*dyb[2])+(((z*(z-1)*(z-2))/fat(3))*dyb[3])

print(f'Para analisar o consumo máximo no intervalo Xi[{xb[0]},{xb[3]}]\n')

print(f'Dada a equação do polinômio: ')
pprint(Eq(eq2, p(13+z)))

print(f'\nCom o objetivo de achar o maior consumo no intervalo de pontos:\n')

derivada1b = solve(Eq(diff(eq2, z, 1), 0), z)
print(f'Aplicando 0 na derivada primeira de {p(13+z)}, as raízes são: {derivada1b}')

derivada2b = [0,0]
derivada2b[0] = diff(eq2, z, 2).subs(z, (derivada1b[0]))
derivada2b[1] = diff(eq2, z, 2).subs(z, (derivada1b[1]))
print(f'Aplicando os pontos {derivada1b} na derivada segunda de {p(13+z)} temos: {derivada2b}')

consumo[2] = eq2.subs(z, (derivada1b[0]))
consumo[3] = eq2.subs(z, (derivada1b[1]))
print(f'\nPortando, dado os pontos de maior e menor consumo em {p((13+derivada1b[0]))} com z={derivada1b[0]} e {p((13+derivada1b[1]))} com z={derivada1b[1]}\nO consumo estimado foi: máx = {consumo[2]}MW e min: {consumo[3]}MW')

ax2.grid()
ax2.scatter((13+derivada1b[0]), consumo[2], c='green', label='Máx')
ax2.scatter((13+derivada1b[1]), consumo[3], c='green', label='Min')
ax2.scatter(xb, yb, c='red', label='Pontos')
ax2.set_title("Gráfico Consumo x Tempo")
b = np.linspace(min(xb), max(xb), 100)
bx = [eq2.subs(z, (xi-xb[0])) for xi in b]
ax2.plot(b, bx, c='purple', label='P(x)')
ax2.set_ylabel('Consumo (MW)')
ax2.set_xlabel('Tempo (h)')
ax2.legend()

print(f'\n==================================\n')

print(f'Tabela dos comsumos máximos e mínimos nos intervalos Xi[{xa[0]},{xa[3]}] e Xi[{xb[0]},{xb[3]}]:')

hora = [0,0,0,0]
hora[0]= tempo(round(5+derivada1a[0],2))
hora[1]= tempo(round(5+derivada1a[1],2))
hora[2]= tempo(round(13+derivada1b[0],2))
hora[3]= tempo(round(13+derivada1b[1],2))

print(f'|Máximo|{hora[0]}|{consumo[0]:.4f}MW|Intervalo Xi[{xa[0]},{xa[3]}]')
print(f'|Mínimo|{hora[1]}|{consumo[1]:.4f}MW|Intervalo Xi[{xa[0]},{xa[3]}]')
print(f'|Máximo|{hora[2]}|{consumo[2]:.4f}MW|Intervalo Xi[{xb[0]},{xb[3]}]')
print(f'|Mínimo|{hora[3]}|{consumo[3]:.4f}MW|Intervalo Xi[{xb[0]},{xb[3]}]')

print(f'\n==================================\n')

plt.show()