
output = []

while True:
    # Setando as informações:
    info: dict[int,int] = {}
    skip = False

    n = int(input())

    for i in range(n):
        line = input().split(" ")
        info[int(line[0])] = int(line[1])

    m = int(input())

    # Condição de parada:
    if n == 0 and m == 0: break

    # Fazendo os testes:
    for i in range(m):
        line = input().split(" ")
        y = int(line[0])
        x = int(line[1])

        # Verificando se não faltam informações:
        qtdAnos = x - y + 1
        for i in range(0,qtdAnos):
            if (qtdAnos + y) not in info.keys():
                skip = True
                break

        if not skip:
            pass

# incompleto

