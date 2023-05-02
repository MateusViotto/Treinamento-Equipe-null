res = []

c: dict[str,float] = {}

while True:
    n = int(input())
    if n == 0:
        break

    for i in range(n):
        entrada = input().split()

        if entrada[2] == 'correct' and entrada[0] not in c.keys():
            c.update([entrada[0],entrada[1]])

    #incompleto