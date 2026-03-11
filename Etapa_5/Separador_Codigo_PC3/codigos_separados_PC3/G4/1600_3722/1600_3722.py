from numpy import*
vet = array(eval(input()))
i = 0
soma = 0
while i < len(vet):
	if vet[i] > 80:
		soma = soma + (vet[i]*85)/100
	else:
		vet[i] = (vet[i]/100)*85
		i = i + 1
	
print(round(soma, 2))		