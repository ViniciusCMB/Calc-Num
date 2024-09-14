import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np
import sympy as sp

x = sp.Symbol('x')

px = np.array([-2, -1, 1, 2])
py = np.array([-1, 0, 0, 1])

pol0 = (-(1/4)*((x+2)**3))+((5/4)*(x+2)) - 1
pol1 = ((1/4)*((x+1)**3))-((3/4)*((x+1)**2))+((1/2)*(x+1))
pol2 = (-(1/4)*((x-1)**3))+((3/4)*((x-1)**2))+((1/2)*(x-1))

function0 = (x+1)**3
function1 = 0*x
function2 = (x-1)**2

def df_dx1(Xi, f):
    df_dx1 = sp.diff(f, x)
    return df_dx1.subs({'x': Xi})

def df_dx2(Xi, f):
    df_dx2 = sp.diff(f, x, 2)
    return df_dx2.subs({'x': Xi})


x0 = np.linspace(-2, -1, 100)
f0 = sp.lambdify((x), function0)
s0 = sp.lambdify((x), pol0)
ys0 = s0(x0)
y0 = f0(x0)
print('='*10)
print('Derivada primeira em x = -1, função0 e S0')
print(df_dx1(-1, function0))
print(df_dx1(-1, pol0))
print('='*10)
print('='*10)
print('Derivada segunda em x = -1, função0 e S0')
print(df_dx2(-1, function0))
print(df_dx2(-1, pol0))
print('='*10)

x1 = np.linspace(-1, 1, 100)
s1 = sp.lambdify((x), pol1)
ys1 = s1(x1)
y1 = np.zeros(len(x1))
print('='*10)
print('Derivada primeira em x = -1, função1 e S1')
print(df_dx1(-1, function1))
print(df_dx1(-1, pol1))
print()
print('Derivada primeira em x = 1, função1 e S1')
print(df_dx1(1, function1))
print(df_dx1(1, pol1))
print('='*10)
print('='*10)
print('Derivada segunda em x = -1, função1 e S1')
print(df_dx2(-1, function1))
print(df_dx2(-1, pol1))
print()
print('Derivada segunda em x = 1, função1 e S1')
print(df_dx2(1, function1))
print(df_dx2(1, pol1))
print('='*10)

x2 = np.linspace(1, 2, 100)
f2 = sp.lambdify((x), function2)
s2 = sp.lambdify((x), pol2)
ys2 = s2(x2)
y2 = f2(x2)
print('='*10)
print('Derivada primeira em x = 1, função2 e S2')
print(df_dx1(1, function1))
print(df_dx1(1, pol1))
print('='*10)
print('='*10)
print('Derivada segunda em x = 1, função2 e S2')
print(df_dx2(1, function2))
print(df_dx2(1, pol2))
print('='*10)

fig = go.Figure()
fig = make_subplots(rows=1, cols=2)

fig.add_trace(go.Scatter(x=x0, y=y0, name=r'$f(x) = (x+1)^3$',
              mode='lines', marker_color='rgba(204,102,0, 255)'), row=1, col=1)
fig.add_trace(go.Scatter(x=x1, y=y1, name=r'$f(x) = 0$',
              mode='lines', marker_color='rgba(204,204,0, 255)'), row=1, col=1)
fig.add_trace(go.Scatter(x=x2, y=y2, name=r'$f(x) = (x-1)^2$',
              mode='lines', marker_color='rgba(102,204,0, 255)'), row=1, col=1)

fig.add_trace(go.Scatter(x=x0, y=ys0, name=r'$S1(x)$', mode='lines',
              marker_color='rgba(0,204,204, 255)'), row=1, col=2)
fig.add_trace(go.Scatter(x=x1, y=ys1, name=r'$S2(x)$', mode='lines',
              marker_color='rgba(0,102,204, 255)'), row=1, col=2)
fig.add_trace(go.Scatter(x=x2, y=ys2, name=r'$S3(x)$', mode='lines',
              marker_color='rgba(0,0,204, 255)'), row=1, col=2)

fig.add_trace(go.Scatter(x=px, y=py, mode='markers', name='Pontos', marker=dict(
    size=20), marker_color='rgba(0, 0, 0, 255)'), row=1, col=1)
fig.add_trace(go.Scatter(x=px, y=py, mode='markers', name='Pontos', marker=dict(
    size=20), marker_color='rgba(0, 0, 0, 255)'), row=1, col=2)

fig.update_layout(title=go.layout.Title(
    text="Interpolação de Spline Cúbica"))

fig.show()