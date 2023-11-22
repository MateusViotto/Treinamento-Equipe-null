nota = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

print('NOTAS:')
for n in notas:
    print('{:.0f} nota(s) de R$ {:.2f}'.format(nota//n, n))
    nota = nota - ((nota//n) * n)
nota = nota * 100
print('MOEDAS:')
for m in moedas:
    print('{:.0f} moeda(s) de R$ {:.2f}'.format(nota // m, m/100))
    nota = nota - ((nota // m) * m)