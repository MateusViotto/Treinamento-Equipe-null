sumDist = 0
cont = 0

while True:
    try:
        input()
        dist = int(input())
        sumDist += dist
        cont += 1
    except:
        break

print(f"{(sumDist/cont).__round__(1)}")
