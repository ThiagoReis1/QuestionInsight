from numpy import*

vet = array(eval(input()))

i = 0

while(i < size(vet)):
	if(vet[i] > 80):
		vet[i] = vet[i] - (vet[i*0.15])
	else:
		vet[i] = vet[i]
	i = i + 1
	
soma = sum(vet)
print(round(soma,2))