from numpy import *

notas = array(eval(input("insira suas notas: ")))
pesos = array([2,1,5])

i = 0
media = 0
soma = 0

if size(notas) == size(pesos):
	while i < size(pesos):
		media = media + (notas[i] * pesos[i])
		soma = soma + pesos[i]
		i = i + 1
	
print(round(media/soma,2))