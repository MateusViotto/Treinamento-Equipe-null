dias = int(input())


anos = dias//365
dias = dias - (anos * 365)
meses = dias // 30
dias = dias - (meses * 30)

print(str(anos) + ' ano(s)')
print(str(meses) + ' mes(es)')
print(str(dias) + ' dia(s)')
