from numpy import*

minimo = 0
maximo = 0 

vet = array(eval(input("digite um vetor:")))

i = 0
qtd = 0
while ( i<size(vet)):
	if((minimo <vet[i]) and (vet[i] <maximo)):
		qtd = qtd + 1
	i = i +1
vet2 = ones(qtd, dtype = float)
i = 0
i2 = 0
while(i<size(vet)):
	if((minimo<vet[i]) and (vet[i]< maximo)):
		i = i + 1
	i2 = i2 + 1
print(vet2)	