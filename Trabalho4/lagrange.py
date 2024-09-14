# Método de lagrange
import numpy as np
import matplotlib.pyplot as plt
fig, (ax1, ax2) = plt.subplots(2, sharex=True) # Cria a figura para o gráfico, sendo dois gráficos que compartilham o eixo x


t = [0, 3, 5, 8, 13, 17]
d = [6, 231, 349, 641, 993, 967]
vn = [68, 67, 51, 78, 71, 79]

v= [] # Calcula a velocidade em milhas por hora
for i in range(len(vn)):
    v.append(vn[i]*0.681818)


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

def d_t(): # Calcula a posição no instante t = 10, imprime o resultado e gera o gráfico
    coef = coef_lagrange(t, d)
    print(f'A posição aproximada pelo Polinômio de Lagrange no instante t=10s é {pol_lagrange(10, t, coef):.4f} pés')
    ax1.grid()
    ax1.scatter(10, pol_lagrange(10, t, coef), c='green', label='T=10')
    ax1.scatter(t, d, c='blue', label='Pontos')
    ax1.set_title("Gráfico PosiçãoxTempo")
    p = np.linspace(min(t), max(t), 100)
    px = [pol_lagrange(xi, t, coef) for xi in p]
    ax1.plot(p, px, c='purple', label='P(x)')
    ax1.set_ylabel('Posição(pés)')
    ax1.legend()



def v_t(): # Calcula a velocidade no instante t = 10, imprime o resultado e gera o gráfico
    coef = coef_lagrange(t, v)
    print(f'A velocidade aproximada pelo Polinômio de Lagrange no instante t=10s é {pol_lagrange(10, t, coef):.4f} milhas/h')
    ax2.grid()
    ax2.scatter(10, pol_lagrange(10, t, coef), c='green', label='T=10')
    ax2.scatter(t, v, c='red', label='Pontos')
    ax2.set_title("Gráfico VelocidadexTempo")
    p = np.linspace(min(t), max(t), 100)
    px = [pol_lagrange(xi, t, coef) for xi in p]
    # print(max(px)) # Printa a velocidade máxima atingida
    ax2.plot(p, px, c='purple', label='P(x)')
    ax2.set_ylabel('Velocidade(milhas/h)')
    ax2.set_xlabel('Tempo(s)')
    ax2.legend()

d_t()
v_t()
plt.show()


