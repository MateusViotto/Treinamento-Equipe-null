n = int(input())
nomes = []
pontos = []
valor = 0

while n != 0:
    meio = n // 2
    printe  = "0"
    for i in range(n):
        nomes.append(input())
    for j in nomes:
        for v in j:
            valor = valor + ord(v)
        pontos.append(valor)
        valor = 0

    for h in range(n):
        timeA = 0
        timeB = 0


        for p in range(meio):
            j = meio - p + 1
            timeA += pontos[p] * j

        for h in range(meio + 1, n):
            j = h - meio
            timeB += pontos[h] * j

        if timeA == timeB:
            printe = str(meio)

        elif timeA > timeB:
            meio = meio - 1

        elif timeA < timeB:
            meio = meio + 1
    if print == "0":
        print('Impossibilidade de empate.')
    else:
        print(printe)
    n = int(input())
