n = int(input())
golB = 0
golG = 0
golR = 0
lista = []
for i in range(n):
    num = int(input())
    for j in range(num):
        gol = input().split(" ")
        if(gol[0] == "R" and gol[1] == "G"):
            golR = golR + 2
        elif(gol[0] == "R" and gol[1] == "B"):
            golR = golR + 1

        if (gol[0] == "G" and gol[1] == "R"):
            golG = golG + 1
        elif (gol[0] == "G" and gol[1] == "B"):
            golG = golG + 2

        if (gol[0] == "B" and gol[1] == "R"):
            golB = golB + 2
        elif (gol[0] == "B" and gol[1] == "G"):
            golB = golB + 1

    if golR > golB and golR > golG:
        lista.append("red")
    elif golG > golB and golG > golR:
        lista.append("green")
    elif golB > golG and golB > golR:
        lista.append("blue")
    elif golB == golG and golG == golR:
        lista.append("trempate")
    elif golB == golG or golB == golR or golG == golR:
        lista.append("empate")

