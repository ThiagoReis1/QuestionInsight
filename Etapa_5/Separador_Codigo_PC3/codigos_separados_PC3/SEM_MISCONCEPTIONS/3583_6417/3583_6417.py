from numpy import *

vet = array(eval(input("Custo dos itens: ")))

total = 0
i = 0
while i < size(vet):
	if(vet[i] > 50):
		total = total + vet[i] - (8 / 100 * vet[i])
	else:
		total = total + vet[i]
	i = i + 1
print(round(total,2))
		