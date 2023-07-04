n = int(input())
x = input().split(' ')
alturas = []
esquerda = []
direita = []
minimo = []

for i in x:
    alturas.append(int(i))

for i in range(n):
    esquerda.append(0)
    direita.append(0)

esquerda[0] = 1
for i in range(1, n):
    esquerda[i] = min(alturas[i], esquerda[i - 1] + 1)
    #print(esquerda[i])


direita[n - 1] = 1

for i in range(n - 2, -1, -1):
    direita[i] = min(alturas[i], direita[i + 1] + 1)


for i in range(n):
    minimo.append(min(esquerda[i], direita[i]))
print(max(minimo))