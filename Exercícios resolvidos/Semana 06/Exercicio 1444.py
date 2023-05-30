entrada = int(input())

while entrada > 0:
    saida = 0
    while entrada > 1:
        if entrada % 3 == 0:
            entrada = entrada / 3
        else:
            entrada = int(entrada / 3) + 1

        saida = saida + entrada
    print(int(saida))
    entrada = int(input())