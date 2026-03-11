from numpy import *

vet = array(eval(input()))

i = 0
qtd = 0
while (i < size(vet)):
	if (-100 <vet[i]):
		qtd = qtd + 1
	i = i + 1
vet2 = ones(qtd, dtype=float)
i = 0
i2 = 0
while (i < size(vet)):
	if (-100 <vet[i]):
		vet2[i2] = vet[i]
		i2 = i2 + 1
	i = i + 1
	
print (vet2)