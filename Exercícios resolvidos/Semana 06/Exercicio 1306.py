n = 0
while True:
    entrada = input().split(" ")
    case = 0
    r, d = entrada
    r = int(r)
    d = int(d)
    n = n + 1
    if r == 0 and d == 0:
        break
    if r > (d * 26):
        print("Case {}: impossible".format(n))
    else:
        while (r/d) > 1:
            case = case + 1
            r = int(r/d)
        print("Case {}: {}".format(n,case))
