palavra = input()
contador = 0
palindromo = True
letras = []
if len(palavra) % 2 == 0:
    for letra in palavra:
        if palavra.count(letra) % 2 != 0:
            palindromo = False
else:
    for letra in palavra:
        if palavra.count(letra) % 2 != 0 and letra not in letras:
            contador = contador + 1
            letras.append(letra)
            if contador == 2:
                palindromo = False
if palindromo:
    print('1')
else:
    print('0')