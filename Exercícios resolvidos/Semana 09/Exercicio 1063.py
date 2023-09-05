while True:

    n=int(input())
    if not n:
        break

    entrada = list(input().split())
    saida = list(input().split())

    pilha = []

    i1=0
    i2 = 0

    result = []

    for s in entrada:
        result += "I",
        pilha.append(s)
        s11 = pilha.pop()
        if saida[i2]==s11:
            result += "R",
            i2 += 1
        else:
            pilha.append(s11)
    while pilha or i2==len(saida)-1:
        s11 = pilha.pop()
        if s11==saida[i2]:
            result += "R",
            i2 += 1
        else:
            break
    if pilha:
        result += " Impossible"
    print("".join(result))