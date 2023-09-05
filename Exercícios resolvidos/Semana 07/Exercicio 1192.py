i = int(input())
entrada = []
saida = []

for y in range(i):
    texto = input()
    entrada.append(texto)

for element in entrada:
    num1 = int(element[0])
    num2 = int(element[2])
    if num1 == num2:
        result = num1 * num2
    elif element[1].isupper():
        result = num2 - num1
    else:
        result = num2 + num1

    saida.append(result)

for x in saida:
    print(x)