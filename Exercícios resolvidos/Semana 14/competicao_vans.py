percurso, velocidade, tempo = map(int, input().split(' '))
distancia = 1000*velocidade*tempo
print(distancia//percurso)
