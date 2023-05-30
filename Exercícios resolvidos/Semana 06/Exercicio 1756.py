n = int(input())
r = []

for i in range(n):
    nbits = int(input())
    linha2 = input().split()
    y = int(linha2[0]) - 1
    p = float(linha2[1])
    q = 1 - p

    paiS = input()
    maeS = input()
    pessoaS = input()

    pai = []
    mae = []
    pessoa = []

    for j in range(nbits):
        pai.append(int(paiS[j]))
        mae.append(int(maeS[j]))
        pessoa.append(int(pessoaS[j]))

    cross1 = []
    cross2 = []

    for j in range(nbits):
        if j <= y:
            cross1.append(pai[j])
            cross2.append(mae[j])
        elif j > y:
            cross1.append(mae[j])
            cross2.append(pai[j])

    dif1 = 0
    dif2 = 0

    for j in range(nbits):
        if cross1[j] != pessoa[j]:
            dif1 += 1

        if cross2[j] != pessoa[j]:
            dif2 += 1

    prob1 = (p**dif1) * (q**(nbits-dif1))
    prob2 = (p**dif2) * (q**(nbits-dif2))
    inter1e2 = (p**(dif1+dif2)) * (q**(2*nbits - dif1 - dif2))
    prob = prob1 + prob2 - inter1e2

    r.append(prob)

for i in r:
    print('%.7f' % i)
