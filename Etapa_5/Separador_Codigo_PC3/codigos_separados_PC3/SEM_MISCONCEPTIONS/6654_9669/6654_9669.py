from numpy import * 

notas = array(eval(input("Entre com as notas: ")))
peso = array([1,3,2,5])

i = 0
soma = 0

while i < size(notas):
	if notas[i] >= 0:
		soma = soma + notas[i] * peso[i]
		media = soma / sum(peso)
	i = i + 1

print(round(media,2))