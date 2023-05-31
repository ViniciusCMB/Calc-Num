#================================================================
def decomp_lu(matriz):
    dim = len(matriz)
    L = [[0] * dim for _ in range(dim)] # Inicializa a matriz L 
    U = [[0] * dim for _ in range(dim)] # Inicializa a matriz U 

    for i in range(dim):
        for j in range(i, dim):
            soma = sum(L[i][k] * U[k][j] for k in range(i)) # Calcula a soma dos produtos dos elementos de L e U
            U[i][j] = matriz[i][j] - soma # Preenche a matriz U com os elementos da matriz original após a subtração

        for j in range(i, dim):
            if i == j:
                L[i][j] = 1 # Preenche a diagonal principal de L com 1
            else:
                soma = sum(L[j][k] * U[k][i] for k in range(i)) # Calcula a soma dos produtos dos elementos de L e U
                L[j][i] = (matriz[j][i] - soma) / U[i][i] # Preenche a matriz L com os elementos da matriz original após a subtração e a divisão

    return L, U  # Retorna as matrizes L e U resultantes da decomposição LU
#================================================================


#================================================================
print('================================')
dimensao = int(input("Digite a dimensão da matriz quadrada A\n" + 
                     "\x1B[3m" + 
                     "(digite '1' para usar a matriz exemplo): ")) # Obtem a dimensão da matriz A quadrada do usuário ou executa a matriz teste

if dimensao == 1: # Executa a matriz teste
    matrizA = [[1, 2, 1], [2, 3, 3], [-3, -10, 2]]

elif dimensao != 1: # Executa a matriz definida pelo usuário
    matrizA = [] # Inicializa a matriz A
    for i in range(dimensao):
        linha = [] # Inicializa as linhas da matriz A
        for j in range(dimensao):
            valor = float(input(f"Digite o valor para a posição A[{i+1}],[{j+1}]: ")) # Obtem os valores dos elementos nas posições i,j
            linha.append(valor) # Preenche as linhas com os valores digitados pelo usuário
        matrizA.append(linha) # Preenche a matriz com as linhas
#================================================================


#================================================================
L, U = decomp_lu(matrizA) # Realiza a decomposição retornando L e U

print('================================')
# Imprime a matriz A
print("A: ")
for linha in matrizA:
    print(linha)

print()
print("=")
print()

# Imprime a matriz L
print("L: ")
for linha in L:
    print(linha)

print()
print("*")
print()

# Imprime a matriz U
print("U: ")
for linha in U:
    print(linha)
print()
print('================================')
#================================================================