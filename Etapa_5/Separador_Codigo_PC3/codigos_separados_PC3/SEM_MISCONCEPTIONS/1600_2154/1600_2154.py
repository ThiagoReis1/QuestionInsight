from numpy import*
from numpy.linalg import*

vet = array(eval(input("vetor de custo dos itens: ")))
total = 0
for j in range(size(vet)):
	if ( vet[j] > 80):
		total = total + (vet[j]*0.85)
	else:
		total = total + vet[j]
print(round(total, 2))