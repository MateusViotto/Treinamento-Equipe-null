while True:
    try:
        entrada = input()
        processos = int(input())
        ciclo = 0
        c = 0

        for i in entrada:
            if i == 'R':
                if c == 0:
                    ciclo = ciclo + 1

                c = c + 1

                if c == processos:
                    c = 0
            else:
                ciclo = ciclo + 1
                c = 0


        print(ciclo)
    except EOFError:
        break