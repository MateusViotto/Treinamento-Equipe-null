n = int(input())
resultados = []

def executa(entrada):
    result = entrada.split(' ')
    resultado = ''
    
    for palavra in result:
        if palavra:
            resultado += palavra[0]
            
    resultados.append(resultado)

for _ in range(n):
    entrada = input()
    executa(entrada)
    
for resultado in resultados: 
    print(resultado)
