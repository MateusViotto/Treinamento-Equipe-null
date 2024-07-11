while True:
    entrada = input().split(' ')
    b, n = entrada
    b = int(b)
    n = int(n)
    saida = 'S'
    if b == 0 and n == 0:
        break

    reserva = list(map(int, input().split(' ')))

    for i in range(n):
        devedor, credor, valor = map(int, input().split())
        reserva[devedor-1] = reserva[devedor-1] - valor
        reserva[credor - 1] = reserva[credor - 1] + valor

    for r in reserva:
        if r < 0:
            saida = 'N'

    print(saida)