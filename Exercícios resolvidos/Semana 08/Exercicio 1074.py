n = int(input())
resultados = []

def validate(value):
    if value == 0:
        result = "NULL"
    elif value > 0:
        if (value % 2) == 0:
            result = "EVEN POSITIVE"
        else:
            result = "ODD POSITIVE"
    else:
        if (value % 2) == 0:
            result = "EVEN NEGATIVE"
        else:
            result = "ODD NEGATIVE"
    resultados.append(result)

for i in range(n):
    entrada = int(input())
    validate(entrada)

for x in range (len(resultados)):
    print(resultados[x])