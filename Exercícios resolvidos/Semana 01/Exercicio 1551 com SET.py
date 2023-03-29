i = int(input())
resultado = []
frases = []
thisset = set() #Declaração do set
for y in range(i):
    texto = input()
    frases.append(texto)

    for letra in frases[y]:
        if letra in "abcdefghijklmnopqrstuvwxyz":
            thisset.add(letra)

if len(thisset) == 26:
    print("frase completa")
elif len(thisset) == 13:
    print("frase quase completa")
elif len(thisset) == 0:
    print("frase mal elaborada")