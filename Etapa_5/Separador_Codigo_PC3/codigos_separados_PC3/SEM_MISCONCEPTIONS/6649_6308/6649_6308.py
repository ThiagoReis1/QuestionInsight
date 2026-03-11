from numpy import *

notas = array(eval(input()))
pesos = array([3.0,2.0,4.0,1.0,3.0])
somatorioPesos = sum(pesos)

i = 0
while(i < size(notas)):
	notas[i] = notas[i] * pesos[i]
	i+=1

somatorio = sum(notas)
media = somatorio/somatorioPesos

print(round(media,2))