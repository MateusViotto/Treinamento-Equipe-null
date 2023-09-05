while True:
    try:
        frase = input().lower().split(" ")
        letra = frase[0][0]
        contador = 0
        flag = True

        for palavra in frase[1:]:



            if palavra[0] == letra:
                if flag:
                    contador = contador + 1
                    flag = False
            else:
                flag = True

            letra = palavra[0]

        print(contador)
    except EOFError:
        break