from numpy import *

vet= array(eval(input(("Digite o vetor de custos:"))))
desc= 0
i= 0

while(i < size(vet)):
	if(vet[i]) > 80:
		desc = desc + vet[i] * 0.15
	i= i + 1
		
print(round(sum(vet) - desc, 2))