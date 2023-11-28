n = int(input())

def acharmmc(a, b):
    while b:
        a, b = b, a % b
    return a

for i in range(n):
    entrada = input().split(' ')
    n1, b1, d1, simb, n2, b2, d2 = entrada
    n1 = int(n1)
    n2 = int(n2)
    d1 = int(d1)
    d2 = int(d2)
    if simb == '+':
        cima = int(((n1 * d2) + (n2 * d1)))
        baixo = int(d1 * d2)

    elif simb == '-':
        cima = int((n1 * d2) - (n2 * d1))
        baixo = int(d1 * d2)

    elif simb == '*':
        cima = n1 * n2
        baixo = d1 * d2

    elif simb == '/':
        cima = int((n1 * d2))
        baixo = int((n2 * d1))

    mmc = acharmmc(cima, baixo)
    print('{}/{} = '.format(cima, baixo), end='')
    if mmc != 0:
        cima = int(cima / mmc)
        baixo = int(baixo / mmc)
    print('{}/{}'.format(cima, baixo), end='\n')
