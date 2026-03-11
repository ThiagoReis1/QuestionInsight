from numpy import *

nota = array(eval(input("insira suas notas: ")))
peso = array([1, 2, 3])

i = 0
num = 0

while i < size(nota):
	num += nota[i] * peso[i]
	i += 1
	
media = num / sum(peso)

print(round(media, 2))