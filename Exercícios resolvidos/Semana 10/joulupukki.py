n = int(input())

begin = 0
r = []

for _ in range(n):

    rascunho = input()

    while True:
        i = rascunho[begin:].find("oulupukk")

        if i == -1:
            break

        if rascunho[i-1] == "J" and rascunho[i+8] == "i":
            begin = i + 8
        else:
            nomeErrado = rascunho[i-1] + "oulupukk" + rascunho[i+8]
            rascunho = rascunho.replace(nomeErrado, "Joulupukki")
            begin = i + 8

    r.append(rascunho)

for i in range(n):
    print(r[i])


# NÃO FUNCIONA