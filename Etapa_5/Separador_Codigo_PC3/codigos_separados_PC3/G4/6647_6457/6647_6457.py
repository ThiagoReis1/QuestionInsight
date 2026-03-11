from numpy import *

nota = array(eval(input("Digite o vetor: ")))

i = 0
peso = [2, 1, 5]
p = 0

while i < size(nota):
	p = p + (peso[i] * nota[i])
	i = i + 1

media = p / sum(peso)
print(round(media, 2))