j=0
n = 1
def obter_consumo(familia):
    return familia['consumo'] // familia['quantidade']

while n != 0:
    j=j+1
    n = int(input())

    familias = []
    for i in range(n):
        p, c = input().split(' ')
        p = int(p)
        c = int(c)
        nova_familia = {'quantidade' : p, 'consumo' : c}
        familias.append(nova_familia)

    familias_ordenadas = sorted(familias, key=obter_consumo)
    consumo_total = 0
    quantidade_total = 0
    print('Cidade# {}:'.format(j))
    for f in familias_ordenadas:
        print('{}-{}'.format(f['quantidade'], (f['consumo'] // f['quantidade'])), end=' ')
        consumo_total = consumo_total + f['consumo']
        quantidade_total = quantidade_total + f['quantidade']

    print('\nConsumo medio: {} m3.'.format(consumo_total/quantidade_total))