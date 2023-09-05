def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mdc_lista(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado = mdc(resultado, numeros[i])
    return resultado

# Solicita a entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Chama a função para encontrar o MDC dos números
resultado = mdc_lista(numeros)

# Exibe o resultado
print("Máximo Divisor Comum:", resultado)
