from numpy import *

notas = array(eval(input()))

peso = 1
media = 0
div = 0
for nota in notas:
	media = media + (nota * peso)
	div = div + peso
	peso = peso + 1
	
media = media / div

print(round(media,2))