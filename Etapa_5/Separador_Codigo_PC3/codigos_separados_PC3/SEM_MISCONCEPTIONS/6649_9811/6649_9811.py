from numpy import *

nota = array(eval(input("notas:")))
pesos = array([3, 2, 4, 1, 3])

i = 0
num = 0

while i < size(nota):
	num += nota[i] * pesos[i]
	i += 1
	
media = num / sum(pesos)
print(round(media, 2))