def crivo_eratostenes(limite):
    primos = [True] * (limite + 1)
    primos[0] = primos[1] = False

    for num in range(2, int(limite**0.5) + 1):
        if primos[num]:
            for mult in range(num*num, limite + 1, num):
                primos[mult] = False

    numeros_primos = [num for num, primo in enumerate(primos) if primo]
    return numeros_primos

# Solicita a entrada do usuário
limite = int(input("Digite o limite superior: "))

# Chama a função para encontrar números primos usando o Crivo de Eratóstenes
numeros_primos = crivo_eratostenes(limite)

# Exibe os números primos encontrados
print("Números primos até", limite, ":", numeros_primos)
