# Função recursiva que primeiro verifica o caminho que está e caso não esteja bloqueado o marca como visitado, então percorre
# todos os seus caminhos vizinhos e os classifica recursivamente, até chegar no final ou não encontrar mais saidas.

def dfs_labirinto(matriz, i, j, visitados):
    # Verificar se está fora dos limites ou se é um obstáculo
    if i < 0 or i >= len(matriz) or j < 0 or j >= len(matriz[0]) or matriz[i][j] == 1:
        return False

     # Verificar se chegou ao final
    if i == len(matriz) - 1 and j == len(matriz[0]) - 1:
        return True

    # Marcar o ponto atual como visitado
    visitados[i][j] = True

     # Explorar os vizinhos (cima, baixo, esquerda, direita)
    if i > 0 and (not visitados[i - 1][j] and dfs_labirinto(matriz, i - 1, j, visitados)):
        return True
    if i < len(matriz) - 1 and (not visitados[i + 1][j] and dfs_labirinto(matriz, i + 1, j, visitados)):
        return True
    if j > 0 and (not visitados[i][j - 1] and dfs_labirinto(matriz, i, j - 1, visitados)):
        return True
    if j < len(matriz[0]) - 1 and (not visitados[i][j + 1] and dfs_labirinto(matriz, i, j + 1, visitados)):
        return True

    return False

# Leitura do número de casos de teste
i = int(input())
saida = []

for _ in range(i):
    # Leitura da matriz de entrada
    matriz = []
    for _ in range(5):
        linha = list(map(int, input().split()))
        matriz.append(linha)

    # Criar uma matriz de visitados com False
    visitados = [[False] * 5 for _ in range(5)]

    # Verificar se há um caminho do início ao final
    tem_caminho = dfs_labirinto(matriz, 0, 0, visitados)

    if tem_caminho:
        saida.append("COPS")
    else:
        saida.append("ROBBERS")

for x in saida:
    print(x)