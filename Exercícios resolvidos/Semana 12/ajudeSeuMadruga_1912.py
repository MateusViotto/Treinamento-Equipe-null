N = 1
res = []

def bb(tiras, area_desejada, sup, inf):

    area_atual = 0
    for tira in tiras:
        if tira > inf:
            area_atual += tira - inf
        else:
            area_atual += 0

    m = (inf + sup)/2

    if abs(area_atual - area_desejada) < 1E-5:
        return m
    elif area_atual > area_desejada:
        return bb(tiras, area_desejada, sup, inf + m/2)
    elif area_atual < area_desejada:
        return bb(tiras, area_desejada, sup, inf - m/2)


while True:
    linha = input().split()
    N = int(linha[0])
    A = int(linha[1])

    if N == 0:
        break

    linha = input().split()
    tiras = [int(tira) for tira in linha]

    if sum(tiras) == A:
        res.append(':D')
    elif sum(tiras) < A:
        res.append('-.-')
    else:
        res.append(bb(tiras, A, max(tiras), 0))

for r in res:
    if type(r) == str:
        print(r)
    else:
        print('{:.4f}'.format(r))

# errado