from numpy import *

peso = [2, 1, 5]

notas = array(eval(input()))
media =0
i =0

while i<3:
	media = media + notas[i]*peso[i]
	i+=1

print(round(media/8,2))