from numpy import*
vet = (array(eval(input("custo dos itens:"))))
i = 0
while(size(vet) > i):
	if(vet[i] > 80):
		vet[i] = vet[i] - (0,15 * vet[i])
	else:
		vet[i] = vet[i]
	i = i + 1
print(round(sum(vet),2))