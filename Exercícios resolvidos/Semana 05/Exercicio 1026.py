r = []

while True:
    try:
        res = ""

        linha = input().split()
        bin1 = bin(int(linha[0])).replace('b','0')
        bin2 = bin(int(linha[1])).replace('b','0')

        if len(bin1) > len(bin2):
            M_bin = bin1
            m_bin = bin2
        else:
            M_bin = bin2
            m_bin = bin1

        if len(m_bin) != len(M_bin):
            for i in range(len(M_bin) - len(m_bin)):
                m_bin = '0' + m_bin

        for i in range(len(M_bin)):
            
            if M_bin[i] == '0':
                if m_bin[i] == '0':
                    res = res + '0'
                else:
                    res = res + '1'
            else:
                if m_bin[i] == '0':
                    res = res + '1'
                else:
                    res = res + '0'

        res = '0b' + res
        res = int(res,base=0)
        r.append(res)

    except EOFError:
        break

for i in range(len(r)):
    print(r[i])