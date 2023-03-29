i = int(input())
frase = []
resultado = []

z=0

for y in range(i):
    texto = input()
    frase.append(texto)

for x in range(i):
    alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    z = z+1
    frase.reverse
    for element in frase[z-1]:
        if element in alfabeto: 
            alfabeto.remove(element)
    resultado.append(len(alfabeto))

print(resultado)

for h in range(i):
    if resultado[h] == 0:
        print("frase completa")

    elif resultado[h] <= 13:
        print("frase quase completa")
        
    elif resultado[h] <=26:
        print("frase mal elaborada")
        



