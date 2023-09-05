def calcular_divisores(numero):
    divisores = [1]  # Começamos com 1, pois todo número é divisível por 1
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            divisores.append(i)
            if i != numero // i:  # Evita adicionar o mesmo divisor duas vezes para números quadrados perfeitos
                divisores.append(numero // i)
    return divisores

def eh_numero_perfeito(numero):
    divisores = calcular_divisores(numero)
    return sum(divisores) == numero

def encontrar_numeros_perfeitos(limit):
    numeros_perfeitos = []
    for i in range(2, limit + 1):
        if eh_numero_perfeito(i):
            numeros_perfeitos.append(i)
    return numeros_perfeitos

# Solicita a entrada do usuário
limite = int(input("Digite um limite superior: "))

# Encontra números perfeitos até o limite fornecido
numeros_perfeitos = encontrar_numeros_perfeitos(limite)

# Exibe os números perfeitos encontrados
print("Números perfeitos encontrados até", limite, ":", numeros_perfeitos)
