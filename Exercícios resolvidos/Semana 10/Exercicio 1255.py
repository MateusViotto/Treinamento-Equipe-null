n = int(input())
lista = dict()
lista2 = []
saida = []
jafoi = []
string = ""
for i in range(n):
    entrada = input().lower().strip()
    entrada = entrada.replace(" ", "")

    for j in entrada:
        lista[j] = entrada.count(j)
        lista2.append([j,entrada.count(j)])

    max1 = lista[max(lista, key= lista.get)]

    for l in lista2:
        if l[1] == max1 and l[0] not in jafoi:
            saida.append(l[0])
            jafoi.append(l[0])

    saida.sort()
    for m in saida:
        string = string + m

    print(string)

    lista.clear()
    lista2.clear()
    saida.clear()
    jafoi.clear()
    string = ""