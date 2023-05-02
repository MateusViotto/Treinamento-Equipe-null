n = int(input())
frases = []

def cortaInverte(value):
    primeiraParte = value[:len(value)//2]
    segundaParte = value[len(value)//2:]
    resultado = primeiraParte[::-1]+segundaParte[::-1]
    frases.append(resultado)

  
for i in range(n):
    entrada = input()
    cortaInverte(entrada)

for x in range (len(frases)):
    print(frases[x])


