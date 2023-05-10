palavra = input()
crib = input()
saida = 0
x = 0
while True:
    k = 0
    daria = True
    for i in crib:
        if crib[k] == palavra[k]:
            daria = False
            break
        k = k + 1
    if daria == True:
        saida = saida + 1
    if len(crib) == len(palavra):
        break

    palavra = palavra[1:]

print(saida)