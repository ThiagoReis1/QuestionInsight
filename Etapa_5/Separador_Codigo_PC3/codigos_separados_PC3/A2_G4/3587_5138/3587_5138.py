#entrada
from numpy import*
p = 100
i = 0 

vet = array(eval(input("Informe os aneis: ")))

while(i < size(vet)):
	if(vet[i] == 1):
		p = p * 5
	if(vet[i] == 2):
		p = p * 3
	if(vet[i] == 3):
		p = p
	if(vet[i] == 4):
		p = p / 2
	i = i + 1

#saida
print(round(p, 2))