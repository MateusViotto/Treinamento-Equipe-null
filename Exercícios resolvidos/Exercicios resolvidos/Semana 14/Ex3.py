n = int(input())


certo = set(range(1, 10))
def funcao(n):
    sudoku1 = []
    sudoku2 = []
    sudoku3 = []
    sudoku4 = []
    sudoku5 = []
    sudoku6 = []
    sudoku7 = []
    sudoku8 = []
    sudoku9 = []
    for k in range(9):
        entrada = input().split(' ')
        entrada = list(map(int, entrada))
        if set(entrada) != certo:
            print('Instancia ' + str(n) + '\n' + 'NAO\n\n')
            return
        if k < 3:
            sudoku1.append(entrada[:3])
            sudoku2.append(entrada[3:6])
            sudoku3.append(entrada[6:])
        elif k < 6:
            sudoku4.append(entrada[:3])
            sudoku5.append(entrada[3:6])
            sudoku6.append(entrada[6:])
        else:
            sudoku7.append(entrada[:3])
            sudoku8.append(entrada[3:6])
            sudoku9.append(entrada[6:])

    sudoku1 = [item for sublist in sudoku1 for item in sublist]
    sudoku2 = [item for sublist in sudoku2 for item in sublist]
    sudoku3 = [item for sublist in sudoku3 for item in sublist]
    sudoku4 = [item for sublist in sudoku4 for item in sublist]
    sudoku5 = [item for sublist in sudoku5 for item in sublist]
    sudoku6 = [item for sublist in sudoku6 for item in sublist]
    sudoku7 = [item for sublist in sudoku7 for item in sublist]
    sudoku8 = [item for sublist in sudoku8 for item in sublist]
    sudoku9 = [item for sublist in sudoku9 for item in sublist]

    s1 = set(sudoku1) == certo
    s2 = set(sudoku2) == certo
    s3 = set(sudoku3)== certo
    s4 = set(sudoku4) == certo
    s5 = set(sudoku5) == certo
    s6 = set(sudoku6) == certo
    s7 = set(sudoku7) == certo
    s8 = set(sudoku8) == certo
    s9 = set(sudoku9) == certo

    if s1 and s2 and s3 and s4 and s5 and s6 and s7 and s8 and s9:
        print('Instancia ' + str(n) + '\n' + 'SIM\n\n')
        return
    else:
        print('Instancia ' + str(n) + '\n' + 'NAO\n\n')
        return

for i in range(n):
    funcao(i+1)

