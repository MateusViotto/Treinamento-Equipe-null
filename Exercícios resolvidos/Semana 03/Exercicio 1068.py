respostas = []

while True:
    try:
        cont = 0
        linha = input()

        for char in linha:

            if char == '(':
                cont += 1
            elif char == ')':
                cont -= 1

            if cont < 0:
                respostas.append("incorrect")
                break
            
        if cont == 0:
            respostas.append("correct")
        elif cont > 0:
            respostas.append("incorrect")

    except EOFError:
        break

for i in range(len(respostas)):
    print(respostas[i])