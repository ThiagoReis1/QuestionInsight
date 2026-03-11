from numpy import *

vet = array(eval(input()))
media = 0
contador = 0
achou_15 = 'false'

for i in range(len(vet)):
	
	if vet[i] > 15.0:
		media = media + vet[i]
		contador = contador + 1
		achou_15 = 'true'
		

	
if achou_15 == 'false':
	print(0.0)
else:
	media = media/contador
	print(round(media, 2))
