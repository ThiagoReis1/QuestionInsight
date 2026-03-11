from numpy import*
notas = array(eval(input()))
peso = array([3,5,1])
i = 0 
media = 0 
soma = 0
if size(notas) == size(peso):
	while i < size(notas):
		media = media + (notas[i]*peso[i])
		soma = soma + peso[i]
		i = i + 1
	print (round(media / soma, 2))