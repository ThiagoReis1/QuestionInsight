from numpy import *

vet= array(eval(input(("Digite o vetor:"))))
desc= 5
i= 0
soma= 0
while(i < size(vet)):
	if(vet[i]) > 80:
		desc = vet[i] - 5
	else:
		desc = vet[i]
	soma= soma + desc
	i= i + 1 

print(round(soma,2))