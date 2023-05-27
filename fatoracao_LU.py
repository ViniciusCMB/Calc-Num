
def LU(A):
    n = len(A)
    x = [0]*n

    # Calculo dos pivos.
    for k in list(range(1, n, 1)):
        # Calculo dos multiplicadores.
        for i in list(range(k+1, n+1, 1)):
            m = A[i-1][k-1]/A[k-1][k-1]
            A[i-1][k-1] = m
            # Atualizar demais valores da linha
            for j in list(range(k+1, n+1, 1)):
                A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1]

    return A

# Resolve o sistema triangular inferior.


def solveLowerTriangular(L, b):
    n = len(b)
    y = [0]*n

    for i in list(range(1, n+1, 1)):
        s = 0
        for j in list(range(1, i, 1)):
            s = s + L[i-1][j-1]*y[j-1]

        y[i-1] = b[i-1] - s

    return y

# Resolve o sistema triangular superior.


def solveUpperTriangular(U, b):
    n = len(b)
    x = [0]*n
    x[n-1] = b[n-1]/U[n-1][n-1]

    for i in list(range(n-1, 0, -1)):
        s = 0
        for j in list(range(i+1, n+1, 1)):
            s = s + U[i-1][j-1]*x[j-1]

        x[i-1] = (b[i-1]-s)/(U[i-1][i-1])

    return x


Tam = int(input('Iforme o tamanho da matriz: '))
Ma = [[0 for i in range(Tam)] for j in range(Tam)]
for i in range(Tam):
    for j in range(Tam):
        Ma[i][j] = float(input(f'Iforme o elemento A[{i+1}][{j+1}]: '))

print('Informe o vetor b: ')
b = []
for j in range(Tam):
    b[j] = float(input(f'Iforme o elemento b[{j+1}]: '))


print(f'Matriz A[{Tam}][{Tam}]: \n')
for i in range(Tam):
    for j in range(Tam):
        print(Ma[i][j], end=' ')
    print()
print()

# Obtendo os fatores L e U.
A = LU(Ma)
print(f'Matriz A[3][3]: \n')
for i in range(len(A)):
    for j in range(len(A)):
        print(A[i][j], end=' ')
    print()
print()

y = solveLowerTriangular(A, b)
print(f'y:', end=' ')

for j in range(len(y)):
    print(y[j], end=' ')
print()


x = solveUpperTriangular(A, y)
print(f'x:', end=' ')
for j in range(len(x)):
    print(x[j], end=' ')
print()
