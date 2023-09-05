from itertools import cycle

nc = int(input())
sobreviventes = []

class Suicida:

    def __init__(self,numero) -> None:
        self.numero = numero
        self.isDead = False

for i in range(nc):
    linha = input().split()
    n = int(linha[0])
    k = int(linha[1])

    suicidasList = [Suicida(i) for i in range(1,n+1)]
    suicidas = cycle(suicidasList)
    countSobreviventes = n

    while countSobreviventes > 1:
        for _ in range(k):
            morto = next(suicidas)

        morto.isDead = True
        countSobreviventes -= 1


print(f"Case {i+1}: {sobreviventes[i]}")