def fatoracao_primos(numero):
    fatores = []

    # Encontra os fatores 2 repetidamente
    while numero % 2 == 0:
        fatores.append(2)
        numero //= 2

    # Encontra os fatores primos ímpares
    for i in range(3, int(numero ** 0.5) + 1, 2):
        while numero % i == 0:
            fatores.append(i)
            numero //= i

    # Se o número remanescente for maior que 2, é um fator primo
    if numero > 2:
        fatores.append(numero)

    return fatores

def representacao_unica(numero):
    fatores = fatoracao_primos(numero)
    fatores_unicos = list(set(fatores))  # Remove duplicatas

    representacao = []
    for fator in fatores_unicos:
        potencia = fatores.count(fator)
        representacao.append((fator, potencia))

    return representacao

# Solicita a entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para obter a representação única do número em termos de fatores primos
resultado = representacao_unica(numero)

# Exibe o resultado
print("Representação única em termos de fatores primos:", resultado)
