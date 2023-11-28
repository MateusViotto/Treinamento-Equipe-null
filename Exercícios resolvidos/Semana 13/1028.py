# Função para calcular o MDC de dois números usando o algoritmo de Euclides
def calcular_mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

for i in range(n):
    a, b = input().split(' ')
    a = int(a)
    b = int(b)
    mdc = calcular_mdc(a, b)
    print(mdc)

