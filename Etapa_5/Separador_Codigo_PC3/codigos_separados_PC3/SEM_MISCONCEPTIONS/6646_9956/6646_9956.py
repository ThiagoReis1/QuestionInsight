from numpy import*
i=0
soma=0
media=0

pesos = [1,2,3]

notas= array(eval(input()))

if size(notas) == size(pesos):
	while i<size(notas):
		media = media + (notas[i]*pesos[i])
		soma = soma + pesos[i]
		i = i + 1
	
print(round(media/soma,2))
	
	