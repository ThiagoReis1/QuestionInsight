inicial = int(input("Posicao inicial do objeto: "))
velocidade = int(input("Velocidade do objeto: "))
tempo = int(input("Tempo de deslocamento: "))

from math import*

limite = 100

final = inicial + (velocidade * tempo)

if (final >= 100):
	print("acima")
else:
	print("ok")

print(final)

