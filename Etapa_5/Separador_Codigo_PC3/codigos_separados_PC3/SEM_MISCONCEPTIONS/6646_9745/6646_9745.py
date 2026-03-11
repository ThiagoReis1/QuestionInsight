from numpy import*

nota = array(eval(input("notas:")))

pesos = array([1,2,3])
i = 0
media = 0
soma = 0

if size(nota) == size(pesos):
	while i < size(nota):
		media = media + (nota[i]*pesos[i])
		soma = soma + pesos[i]
		i += 1
		
	print(round(media/soma,2))