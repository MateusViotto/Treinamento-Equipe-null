n = int(input())
swaps = []
for i in range(n):
    l = int(input())
    entrada = input().split(" ")
    saida = 0
    j = 0
    while entrada != sorted(entrada):
        if entrada[j] > entrada[j+1]:
            v1 = entrada[j]
            v2 = entrada[j+1]
            entrada[j] = v2
            entrada[j+1] = v1
            saida = saida + 1
        j = j + 1
        if j == len(entrada)-1:
            j = 0

    swaps.append(saida)

for g in swaps:
    print("Optimal train swapping takes {} swaps.".format(g))