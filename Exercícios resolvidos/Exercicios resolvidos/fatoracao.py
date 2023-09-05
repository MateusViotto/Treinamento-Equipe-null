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

# Solicita a entrada do usuário
numero = int(input("Digite um número inteiro: "))

# Chama a função para realizar a fatoração
resultado = fatoracao_primos(numero)

# Exibe o resultado
print("Fatores primos:", resultado)
