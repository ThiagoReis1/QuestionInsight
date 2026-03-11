from numpy import *

notas = array(eval(input('')))
vet = array([3,5,1])

i = 0
cont = 0

while i < size(notas):
	cont += notas[i] * vet[i]
	i += 1
	
media = cont / sum(vet)
print(round(media,2))