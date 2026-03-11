from numpy import*

vet = array(eval(input()))
pesos = [5,4,3,2]
soma = 0

i = 0
while(i < size(vet)):
	if(i == 0):
		soma = soma + (vet[i] * pesos[i])
	if(i == 1):
		soma = soma + (vet[i] * pesos[i])
	if(i == 2):
		soma = soma + (vet[i] * pesos[i])
	if(i == 3):
		soma = soma + (vet[i] * pesos[i])
	i = i + 1
mp = soma/sum(pesos)
print(round(mp, 2))