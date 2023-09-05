entrada = input('')

x = entrada.count('X')
flag = False
ponto = 0
saida = '?'
if x < 2:
    print('?')
else:
    if entrada.count('XX') == 1:
        saida = 'Alice'
        if entrada.count('XXX') == 1:
            saida = '?'
    elif entrada.count('OO') == 1:
        saida = '?'

    else:
        saida = '*'

    print(saida)

