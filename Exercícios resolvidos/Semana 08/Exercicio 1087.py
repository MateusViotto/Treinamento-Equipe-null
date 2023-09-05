entrada = []
inicio = []
fim = []
resultado = []

while True:
    i = input()
    if i == '0 0 0 0':
        break

    entrada = list(map(int, i.split()))
    inicio.append(entrada[:2])
    fim.append(entrada[-2:])

    if inicio[-1] == fim[-1]:
        resultado.append(0)
    elif inicio[-1][0] == fim[-1][0]:
        resultado.append(1)
    elif inicio[-1][1] == fim[-1][1]:
        resultado.append(1)
    elif abs(inicio[-1][0] - fim[-1][0]) == abs(inicio[-1][1] - fim[-1][1]):
        resultado.append(1)
    else:
        resultado.append(2)

for result in resultado:
    print(result)