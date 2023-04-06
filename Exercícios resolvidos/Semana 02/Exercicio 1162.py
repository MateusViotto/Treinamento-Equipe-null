n = int(input())
saida = []
while n > 0:
    n -= 1
    l = int(input())
    vagao = input().split()

    swap = 0
    for i in range(l):
        for j in range(i + 1, l):
            if (int(vagao[i]) > int(vagao[j])):
                vagao[i], vagao[j] = vagao[j], vagao[i]
                swap = swap + 1
    saida.append(swap)
for x in saida:
    print('Optimal train swapping takes %d swaps.' % x)