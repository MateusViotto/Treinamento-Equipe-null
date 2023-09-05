def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

def mmc(a, b):
    return (a * b) // mdc(a, b)

def mmc_lista(numeros):
    resultado = numeros[0]
    for i in range(1, len(numeros)):
        resultado = mmc(resultado, numeros[i])
    return resultado

# Solicita a entrada do usuário
entrada = input("Digite os números separados por espaço: ")
numeros = list(map(int, entrada.split()))

# Chama a função para encontrar o MMC dos números
resultado = mmc_lista(numeros)

# Exibe o resultado
print("Mínimo Múltiplo Comum:", resultado)
