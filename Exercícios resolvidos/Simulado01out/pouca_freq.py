n = int(input())
saida = ''
for treco in range(n):
    m = int(input())
    alunos = input().split(' ')
    presencas = input().split(' ')
    faltosos = ''
    for i in range(m):
        aluno = alunos[i]
        presenca = presencas[i]

        total = 0
        faltas = 0
        for letra in presenca:
            if letra == 'A':
                total+=1
                faltas+=1
            elif letra == 'P':
                total+=1

        if faltas/total > 0.25:
            if faltosos:
                faltosos = faltosos + f' {aluno}'
            else:
                faltosos = f'{aluno}'

    if treco == n - 1:
        saida = saida + faltosos
    else:
        saida = saida + faltosos + '\n'

print(saida)
