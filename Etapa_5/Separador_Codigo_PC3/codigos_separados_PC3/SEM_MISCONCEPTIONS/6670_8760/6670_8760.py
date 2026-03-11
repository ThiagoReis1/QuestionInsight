from numpy import *

vet = array(eval(input("")))

media = 0
g = 0

for i in range(size(vet)):
	if vet[i] > 20.00: 
		media = media + vet[i]
		g = g + 1
		
if g == 0:
	print(0.0)
else:
	print(round(media / g, 2))

