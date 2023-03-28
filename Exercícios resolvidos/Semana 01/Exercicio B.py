caso = int(input())
i = 0
XXL = []
XL = []
L = []
M = []
S = []
XS = []
saida = []
while i < caso:
    g = 1
    entrada = input().split(" ")
    n, m = entrada
    n = int(n)
    m = int(m)
    nCamisas = n/6
    for j in range(0,m):
        entrada2 = input().split(" ")
        tm1, tm2 = entrada2
        if tm1 == "XXL":
            XXL.append(tm1)
            if tm2 == "XL":
                XL.append(tm2)
            if len(XXL) > nCamisas and len(XL) > nCamisas:
                saida.append("NO")
                g = 0
        if tm1 == "XL":
            XL.append(tm1)
            if tm2 == "XXL":
                XXL.append(tm2)
            elif tm2 == "L":
                L.append(tm2)
            if len(XXL) > nCamisas and len(XL) > nCamisas:
                saida.append("NO")
                g = 0
            elif len(XL) > nCamisas and len(L) > nCamisas:
                saida.append("NO")
                g = 0

        if tm1 == "L":
            L.append(tm1)
            if tm2 == "XL":
                XL.append(tm2)
            elif tm2 == "M":
                M.append(tm2)
            if len(M) > nCamisas and len(L) > nCamisas:
                saida.append("NO")
                g = 0
            elif len(L) > nCamisas and len(XL) > nCamisas:
                saida.append("NO")
                g = 0

        if tm1 == "M":
            M.append(tm1)
            if tm2 == "L":
                L.append(tm2)
            elif tm2 == "S":
                S.append(tm2)
            if len(M) > nCamisas and len(S) > nCamisas:
                saida.append("NO")
                g = 0
            elif len(M) > nCamisas and len(L) > nCamisas:
                saida.append("NO")
                g = 0

        if tm1 == "S":
            S.append(tm1)
            if tm2 == "M":
                M.append(tm2)
            elif tm2 == "XS":
                XS.append(tm2)
            if len(XS) > nCamisas and len(S) > nCamisas:
                saida.append("NO")
                g = 0
            elif len(S) > nCamisas and len(M) > nCamisas:
                saida.append("NO")
                g = 0

        if tm1 == "XS":
            XS.append(tm1)
            if tm2 == "S":
                S.append(tm2)
            if len(XS) > nCamisas and len(S) > nCamisas:
                saida.append("NO")
                g = 0


    i = i + 1
    if g == 1:
        saida.append("YES")

    XXL.clear()
    XL.clear()
    L.clear()
    M.clear()
    S.clear()
    XS.clear()

for k in saida:
    print(k)
