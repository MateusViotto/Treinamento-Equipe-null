algarismos = [int(letra) for letra in input()]
soma_par = 0
soma_impar = 0

for algarismo in algarismos:

    if algarismo%2 == 0:
        soma_par += algarismo
    else:
        soma_impar += algarismo

if (soma_par/3).is_integer():
    print('S')
else:
    print('N')

if (soma_impar/3).is_integer():
    print('S')
else:
    print('N')
