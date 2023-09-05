lista = []

resultado = []

while True:
    try:
        economizou = 0
        n = int(input())

        for i in range(n):
            x = input()
            lista.append(x)

        for y in range(n - 1):
            for z in range(len(lista[0])):
                if lista[y][z] == lista[y-1][z]:
                    economizou = economizou + 1
                else:
                    break

        print(economizou)

        y = 0
        z = 0
        lista.clear()
    except EOFError:
        break