from sympy import *
import numpy as npy
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
fig, (ax1, ax2) = plt.subplots(2, sharex=True) # Cria a figura para o gráfico, sendo dois gráficos que compartilham o eixo x

init_printing(pretty_print=True)
r = Symbol('r')
f = Symbol('F')
v = symbols('V', cls = Function)
Z = Symbol('Z')

a, b, c = 0, 4, 2

eq1 = r*cos(r)
eq2 = 2*pi*Integral(v(r), r)

print('Dada as expressões:\n')
pprint(Eq(eq1, v(r)))
pprint(Eq(eq2, f))

print(f'\n==================================')

def st_simp(y, h, ni, np):

    y_impar = [y[i] for i in range(1, np, 2)]
    y_par = [y[i] for i in range(2, ni, 2)]

    soma_impar = 0.0
    soma_par = 0.0

    for k in range(len(y_impar)):
        soma_impar += y_impar[k]

    for k in range(len(y_par)):
        soma_par += y_par[k]
    return (h/3)*(y[0]+(4*soma_impar)+(2*soma_par)+y[len(y)-1])

def erro_st_simp(f, i, n):
    return -(((f-i)**5)/(180*(n**4)))*((diff(eq1, r, 4)).subs(r, i)).evalf(), -(((f-i)**5)/(180*(n**4)))*((diff(eq1, r, 4)).subs(r, f)).evalf()

def nd_simp(y, h):

    soma_ci_1 = 0.0
    soma_ci_2 = 0.0
    soma_ci_3 = 0.0

    for i in range(len(y)):
        if i == 0 or i == len(y)-1:
            soma_ci_1 += y[i]
        elif i%3 == 0 and i!=0 and i!=len(y)-1:
            soma_ci_2 += y[i]
        else:
            soma_ci_3 += y[i]

    return (3*h/8)*(soma_ci_1+(2*soma_ci_2)+(3*soma_ci_3))

def erro_nd_simp(f, i, n):
    return -(((f-i)**5)/(80*(n**4)))*((diff(eq1, r, 4)).subs(r, i)).evalf(), -(((f-i)**5)/(80*(n**4)))*((diff(eq1, r, 4)).subs(r, f)).evalf()

def trapezio(y, h):
    soma_ci_1 = 0.0
    soma_ci_2 = 0.0

    for i in range(len(y)):
        if i == 0 or i == len(y)-1:
            soma_ci_1 += y[i]
        else:
            soma_ci_2 += y[i]

    return (h/2)*(soma_ci_1+(2*soma_ci_2))

def erro_trapezio(f, i, h):
    return -(((f-i)*(h**2))/12)*((diff(eq1, r, 2)).subs(r, i)).evalf(), -(((f-i)*(h**2))/12)*((diff(eq1, r, 2)).subs(r, f)).evalf()

def calc_h(f, i, n):
    return (f-i)/n

def calc_dy(x, y): # Calcula o delta y
    pontos = len(x)
    Y = [item for item in y]
    dy = npy.zeros(pontos)
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

def calc_pol(z, dy):
    pontos = len(dy)
    s = 0
    for i in range(pontos):
        prod = 1
        for j in range(i):
                prod *= (z-j)
        prod *= dy[i]/fat(i)
        s += prod
    return s

def calc_pol_str(dy):
    pontos = len(dy)
    s = 0
    for i in range(pontos):
        prod = 1
        for j in range(i):
                prod *= (Z-j)
        prod *= dy[i]/fat(i)
        s += prod
    return s

def Qa():
    yi = [0, 1.47, 2.87, 4.20, 5.43, 6.31, 7.07, 7.62, 7.77, 7.83, 8.27, 8.43, 8.79, 0]
    print('A)')

    #  Para o intervalo [0,2] com 5 pontos e 4 subintervalos
    np = 5
    ni = np - 1
    yi1 = [yi[i] for i in range(np)]
    xi1 = [i*(2/4) for i in range(np)]
    print(f'Para o intervalo de 5 pontos em [0,2], Yi={yi1}')
    print('Com o polinômio interpolador:')
    pprint(expand(calc_pol_str(calc_dy(xi1, yi1))))
    print('\n')
    integ1 = st_simp(yi1, calc_h(c, a, ni), ni, np)*2*pi
    interv_erro1spi1, interv_erro1spf1 = erro_st_simp(c, a, ni)
    integ2 = nd_simp(yi1, calc_h(c, a, ni))*2*pi
    interv_erro2spi1, interv_erro2spf1 = erro_nd_simp(c, a, ni)
    print(f'O valor da integral utilizando a 1ª Regra de Simpson é {integ1:.4f}, com erro no intervalo ]{interv_erro1spi1:.4f},{interv_erro1spf1:.4f}[')
    print(f'O valor da integral utilizando a 2ª Regra de Simpson é {integ2:.4f}, com erro no intervalo ]{interv_erro2spi1:.4f},{interv_erro2spf1:.4f}[')

    #  Para o intervalo [2,4] com 10 pontos e 9 subintervalos
    np = 10
    ni = np - 1
    yi2 = [yi[i+4] for i in range(np)]
    xi2 = [2+((i)*((4-2)/9)) for i in range(np)]
    print(f'\nE, para o intervalo de 10 pontos em [2,4], Yi={yi2}')
    print('Com o polinômio interpolador:')
    pprint(expand(calc_pol_str(calc_dy(xi2, yi2))))
    print('\n')
    integ3 = st_simp(yi2, calc_h(b, c, ni), ni, np)*2*pi
    interv_erro1spi2, interv_erro1spf2 = erro_st_simp(b, c, ni)
    integ4 = nd_simp(yi2, calc_h(b, c, ni))*2*pi
    interv_erro2spi2, interv_erro2spf2 = erro_nd_simp(b, c, ni)
    print(f'O valor da integral utilizando a 1ª Regra de Simpson é {integ3:.4f}, com erro no intervalo ]{interv_erro1spi2:.4f},{interv_erro1spf2:.4f}[')
    print(f'O valor da integral utilizando a 2ª Regra de Simpson é {integ4:.4f}, com erro no intervalo ]{interv_erro2spi2:.4f},{interv_erro2spf2:.4f}[')
 
    print('\n')
    print(f'   A vazão total que se obtem utilizando a 1ª Regra de Simpson nos intervalos desejados é {integ1 + integ3:.4f}, com erro no intervalo ]{interv_erro1spi1+interv_erro1spi2:.4f},{interv_erro1spf1+interv_erro1spf2:.4f}[')
    print(f'   A vazão total que se obtem utilizando a 2ª Regra de Simpson nos intervalos desejados é {integ2 + integ4:.4f}, com erro no intervalo ]{interv_erro2spi1+interv_erro2spi2:.4f},{interv_erro2spf1+interv_erro2spf2:.4f}[')    

    ax1.set_title("Gráfico Xi x Yi - (A)")
    ax1.set_ylim(bottom=0, top=10)

    p1 = npy.linspace(min(xi1), max(xi1), 100)
    px1 = [calc_pol(calc_z(i, xi1), calc_dy(xi1, yi1)) for i in p1]
    ax1.plot(p1, px1, c='purple', label=f'P(x)[{a},{c}]')

    p2 = npy.linspace(min(xi2), max(xi2), 100)
    px2 = [calc_pol(calc_z(i, xi2), calc_dy(xi2, yi2)) for i in p2]
    ax1.plot(p2, px2, c='indigo', label=f'P(x)[{c},{b}]')

    verts1 = [(a, 0), *zip(p1, px1), (b, 0)]
    poly1 = Polygon(verts1, facecolor='cornflowerblue')
    ax1.add_patch(poly1)

    verts2 = [(a, 0), *zip(p2, px2), (b, 0)]
    poly2 = Polygon(verts2, facecolor='cornflowerblue')
    ax1.add_patch(poly2)

    ax1.scatter(xi1, yi1, c='red', label='Pontos')
    ax1.scatter(xi2, yi2, c='red', label=None)
    ax1.set_ylabel('Y')
    ax1.text(0.5 * (a + b + 1), ((max(yi)+min(yi))/2)-2, rf'${latex(eq2)}$'+f' ≈ {integ1 + integ3:.4f}',
        horizontalalignment='center', fontsize=15)
    ax1.legend()

    return print(f'\n==================================')
    
def Qb():
    yi = [0, 1.471, 2.879, 4.207, 5.434, 6.316, 7.072, 7.628, 7.77, 0]
    print('B)')

    #  Para o intervalo [0,2] com 5 pontos e 4 subintervalos
    np = 5
    ni = np - 1
    yi1 = [yi[i] for i in range(np)]
    xi1 = [i*(2/4) for i in range(np)]
    print(f'Para o intervalo de 5 pontos em [0,2], Yi={yi1}')
    print('Com o polinômio interpolador:')
    pprint(expand(calc_pol_str(calc_dy(xi1, yi1))))
    print('\n')
    integ1 = trapezio(yi1, calc_h(c, a, ni))*2*pi
    interv_erroti1, interv_errotf1 = erro_trapezio(c, a, calc_h(c, a, ni))
    integ2 = st_simp(yi1, calc_h(c, a, ni), ni, np)*2*pi
    interv_erro1spi1, interv_erro1spf1 = erro_st_simp(c, a, ni)
    print(f'O valor da integral utilizando a Regra dos Trapézios é {integ1:.4f}, com erro no intervalo ]{interv_erroti1:.4f},{interv_errotf1:.4f}[')
    print(f'O valor da integral utilizando a 1ª Regra de Simpson é {integ2:.4f}, com erro no intervalo ]{interv_erro1spi1:.4f},{interv_erro1spf1:.4f}[')

    #  Para o intervalo [2,4] com 10 pontos e 9 subintervalos
    np = 6
    ni = np - 1
    yi2 = [yi[i+4] for i in range(np)]
    xi2 = [2+((i)*((4-2)/5)) for i in range(np)]  
    print(f'\nE, para o intervalo de 6 pontos em [2,4], Yi={yi2}')
    print('Com o polinômio interpolador:')
    pprint(expand(calc_pol_str(calc_dy(xi2, yi2))))
    print('\n')
    integ3 = trapezio(yi2, calc_h(b, c, ni))*2*pi
    interv_erroti2, interv_errotf2 = erro_trapezio(b, c, calc_h(b, c, ni))
    integ4 = st_simp(yi2, calc_h(b, c, ni), ni, np)*2*pi
    interv_erro1spi2, interv_erro1spf2 = erro_st_simp(b, c, ni)
    print(f'O valor da integral utilizando a Regra dos Trapézios é {integ3:.4f}, com erro no intervalo ]{interv_erroti2:.4f},{interv_errotf2:.4f}[')
    print(f'O valor da integral utilizando a 1ª Regra de Simpson é {integ4:.4f}, com erro no intervalo ]{interv_erro1spi2:.4f},{interv_erro1spf2:.4f}[')
    
    print('\n')
    print(f'   A vazão total que se obtem utilizando a Regra dos Trapézios nos intervalos desejados é {integ1 + integ3:.4f}, com erro no intervalo ]{interv_erroti1+interv_erroti1:.4f},{interv_erro1spi1+interv_erro1spi2:.4f}[')
    print(f'   A vazão total que se obtem utilizando a 1ª Regra de Simpson nos intervalos desejados é {integ2 + integ4:.4f}, com erro no intervalo ]{interv_erro1spi1+interv_erro1spi2:.4f},{interv_erro1spf1+interv_erro1spf2:.4f}[')    

    ax2.set_title("Gráfico Xi x Yi - (B)")
    ax2.set_ylim(bottom=0, top=10)

    p1 = npy.linspace(min(xi1), max(xi1), 100)
    px1 = [calc_pol(calc_z(i, xi1), calc_dy(xi1, yi1)) for i in p1]
    ax2.plot(p1, px1, c='purple', label=f'P(x)[{a},{c}]')

    p2 = npy.linspace(min(xi2), max(xi2), 100)
    px2 = [calc_pol(calc_z(i, xi2), calc_dy(xi2, yi2)) for i in p2]
    ax2.plot(p2, px2, c='indigo', label=f'P(x)[{c},{b}]')

    verts1 = [(a, 0), *zip(p1, px1), (b, 0)]
    poly1 = Polygon(verts1, facecolor='lightcoral')
    ax2.add_patch(poly1)
    verts2 = [(a, 0), *zip(p2, px2), (b, 0)]
    poly2 = Polygon(verts2, facecolor='lightcoral')
    ax2.add_patch(poly2)

    ax2.scatter(xi1, yi1, c='blue', label='Pontos')
    ax2.scatter(xi2, yi2, c='blue', label=None)

    ax2.set_ylabel('Y')
    ax2.set_xlabel('X')
    ax2.text(0.5 * (a + b + 1), ((max(yi)+min(yi))/2)-2, rf'${latex(eq2)}$'+f' ≈ {integ2 + integ4:.4f}',
        horizontalalignment='center', fontsize=15)
    ax2.legend()
    plt.show()

    return print(f'\n==================================') 

Qa()
Qb()