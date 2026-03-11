from numpy import *
vet = array(eval(input("vetor de custo: ")))
i = 0
pfinal = 0

while (i < size(vet)):
	if (vet[i] > 80):
		pfinal = pfinal + vet[i] - (vet[i])*(15/100)
	else:
		pfinal = pfinal + vet[i]
	i = i + 1
	
print(round(pfinal, 2))