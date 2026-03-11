from numpy import *

notas = array(eval(input()))
pesos = array([2,2,6,1])

i = 0
somaNotas = 0

while i < size(pesos):
	somaNotas += (notas[i]*pesos[i])
	i += 1

media = somaNotas/sum(pesos)
print(round(media, 2))
	