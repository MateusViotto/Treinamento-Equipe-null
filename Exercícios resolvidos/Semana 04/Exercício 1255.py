n = int(input())

for i in range(n):
    frase = input().lower()
    lista = {}
    for c in frase:
        if c.isalpha() and c not in lista:
            lista[c] = frase.count(c)
    listaordenada = sorted(lista.items(), key=lambda x: (-x[1],x[0]))
    saida = ''
    for c in listaordenada:
        if c[1] == listaordenada[0][1]:
            saida += c[0]
        else:
            break
    print(saida)