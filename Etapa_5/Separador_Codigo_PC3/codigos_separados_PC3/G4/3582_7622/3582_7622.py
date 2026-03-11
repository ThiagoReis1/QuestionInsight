from numpy import *

vet = array(eval(input("custo dos itens: ")))

i = 0

while i < size(vet):
	if vet[i] > 160.0:
		vet[i] -= 25
	i += 1
print(round(sum(vet),2))