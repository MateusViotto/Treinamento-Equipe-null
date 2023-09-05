#Input: r1, x1, y1, r2, x2, y2

#C1 deve conter C2 para RICO, caso contrário MORTO

import math

def distPontos(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

respostas = []

while True:
    try:
        list = input().split()
        r1,x1,y1,r2,x2,y2 = [int(val) for val in list]
        distC1C2 = distPontos(x1,y1,x2,y2)
        if distC1C2 + r2 <= r1:
            respostas.append("RICO")
        else:
            respostas.append("MORTO")
    except EOFError:
        break

for r in respostas:
    print(r)