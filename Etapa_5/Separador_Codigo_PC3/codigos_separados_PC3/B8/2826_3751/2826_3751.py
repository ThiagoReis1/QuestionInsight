from numpy import *

notas = array(eval(input()))

i = 0
tam = len(notas)
while i < tam:
	if notas[i] > 8:
		notas[i] = 10
	elif notas[i] < 2:
		notas[i] = 0
	i += 1

print(notas)