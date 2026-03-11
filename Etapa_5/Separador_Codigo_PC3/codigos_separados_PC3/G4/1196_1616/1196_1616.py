from numpy import *

minimo = -60
maximo = 60

vet = array(eval(input("Informe o vetor: ")))

i = 0
qtd = 0
while (i < size(vet)):
	if ((minimo <vet[i]) and (vet[i] < maximo)):
		qtd = qtd + 1
	i = i + 1
vet2 = ones(qtd, dtype=float)
i = 0
i2 = 0
while (i < size(vet)):
	if ((minimo <vet[i]) and (vet[i] < maximo)):
		vet2[i2] = vet[i]
		i2 = i2 + 1
	i = i + 1
	
print (vet2)