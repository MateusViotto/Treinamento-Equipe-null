def mdc_estendido(a, b):
    if a == 0:
        return b, 0, 1
    else:
        mdc, x, y = mdc_estendido(b % a, a)
        return mdc, y - (b // a) * x, x


def teorema_resto_chines(residuos, modulos):
    n = len(modulos)

    # Calcula o produto de todos os módulos
    N = 1
    for modulo in modulos:
        N *= modulo

    # Calcula as constantes de cada equação
    constantes = []
    for modulo in modulos:
        Ni = N // modulo
        _, inverso, _ = mdc_estendido(Ni, modulo)
        constantes.append(inverso * Ni)

    # Calcula a solução usando o Teorema do Resto Chinês
    x = sum(residuos[i] * constantes[i] for i in range(n)) % N

    return x


# Solicita a entrada do usuário
n = int(input("Digite o número de congruências: "))
residuos = []
modulos = []

for i in range(n):
    residuo = int(input(f"Digite o {i + 1}º residuo: "))
    modulo = int(input(f"Digite o {i + 1}º módulo: "))
    residuos.append(residuo)
    modulos.append(modulo)

# Chama a função para resolver o sistema de congruências usando o Teorema do Resto Chinês
resultado = teorema_resto_chines(residuos, modulos)

# Exibe o resultado
print("A solução do sistema de congruências é:", resultado)
