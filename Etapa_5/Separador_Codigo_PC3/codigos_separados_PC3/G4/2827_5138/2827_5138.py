#entrada 
from numpy import*
i = 0
vet = array(eval(input("Informe as notas: ")))

while(i < size(vet)):
	if((vet[i] > 9) and (vet[i] < 10)):
		vet[i] = 10
	if((vet[i] > 4) and (vet[i] < 5)):
		vet[i] = 4
	i = i + 1
	
#saida
print(vet)