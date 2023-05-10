entrada = input().split(" ")
interr, lamp = entrada
interr = int(interr)
lamp = int(lamp)
lampada = []
listaInterr = []
saida = 0
impossivel = 1
for i in range(lamp):
    lampada.append(-1)

acessas = input().split(" ")
acessas = acessas[1:]
for j in acessas:
    lampada[int(j) - 1] = 1

list = lampada.copy()

for i in range(interr):
    listaInterr.append(input().split(" "))

while True:

    if 1 not in lampada:
        break
    if impossivel == -1:
        saida = impossivel
        break
    for p in range(len(listaInterr) - 1):
        saida = saida + 1
        for e in listaInterr[p][1:]:
            e = int(e)
            lampada[e-1] = lampada[e-1] * (-1)

            if lampada == list:
                impossivel = -1
                break

print(saida)