from numpy import *

pesos = [1,3,2,5]
i = 0
nota = 0
notas = array(eval(input("Digite as notas: ")))

while (i < size(notas)):
	nota = nota + (notas[i] * pesos[i])
	i = i + 1
	
e = sum(pesos)
media = nota / e
 
print (round(media,2))
