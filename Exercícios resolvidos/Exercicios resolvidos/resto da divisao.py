def resolver_congruencia(valor, modulo):
    resto = valor % modulo
    return resto

# Solicita a entrada do usuário
valor = int(input("Digite o valor: "))
modulo = int(input("Digite o módulo: "))

# Chama a função para resolver a congruência
resultado = resolver_congruencia(valor, modulo)

# Exibe o resultado
print(f"O resto da congruência {valor} % {modulo} é {resultado}.")
