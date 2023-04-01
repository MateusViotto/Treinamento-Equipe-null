i = int(input())

frases = []
thisset = set() #Declaração do set
saida = []
for y in range(i):
    texto = input()
    frases.append(texto)

    for letra in frases[y]:
        if letra in "abcdefghijklmnopqrstuvwxyz":
            thisset.add(letra)

    if len(thisset) <= 13:
        saida.append("frase mal elaborada")
    elif len(thisset) <= 25:
        saida.append("frase quase completa")
    elif len(thisset) == 26:
        saida.append("frase completa")
    thisset.clear()
for msg in saida:
    print(msg)