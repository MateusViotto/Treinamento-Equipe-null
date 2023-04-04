n = 1
n = int(input())
lista = []
saida = []
while n != 0:

    entrada1 = []

    for i in range(n):
        nome = input()
        entrada2 = input().split(" ")
        cor, tamanho = entrada2
        entrada1.append(cor)
        entrada1.append(tamanho)
        entrada1.append(nome)
        lista.append(entrada1.copy())
        entrada1.clear()
    lista.sort(key=lambda x: x[2])
    lista.sort(reverse=True, key=lambda x: x[1])
    lista.sort(key=lambda x: x[0])  # Função anônima
    for j in lista:
        saida.append("{} {} {}".format(j[0], j[1], j[2]))
    lista.clear()
    n = int(input())
    saida.append("PularLinha")

for m in saida:
    print(m)

