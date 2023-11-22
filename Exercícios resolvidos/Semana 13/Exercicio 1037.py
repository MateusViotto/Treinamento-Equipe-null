n = float(input())
saida = '0'
if n >= 0 and n <= 25:
    saida = 'Intervalo [0,25]'
elif n > 25 and n <= 50:
    saida = 'Intervalo (25,50]'
elif n > 50 and n <= 75:
    saida = 'Intervalo (50,75]'
elif n > 75 and n <= 100:
    saida = 'Intervalo (75,100]'
else:
    saida = 'Fora de intervalo'

print(saida)
