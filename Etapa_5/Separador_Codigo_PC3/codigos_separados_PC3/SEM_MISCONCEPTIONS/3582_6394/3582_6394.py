from numpy import *

vet = array(eval(input("Digite os custos dos itens: ")))
i = 0
total = 0

while(i < size(vet)):
	if(vet[i] > 160):
		total = total + (vet[i] - 25)
	else:
		total = total + vet[i]
		
	i += 1
	
print(round(total, 2))