from math import floor

res = []

while True:
    try:
        num = float(input())
        cutoff = float(input())

        base = floor(num)
        dec = num - base

        if dec >= cutoff:
            base += 1

        res.append(base)

    except EOFError:
        break

for i in range(len(res)):
    print(res[i])