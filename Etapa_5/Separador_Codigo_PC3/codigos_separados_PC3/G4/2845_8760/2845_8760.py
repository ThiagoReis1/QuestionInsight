from numpy import *

vet = array(eval(input("")))
i= 0
for i in size(vet):
	if vet[i] == 0:
		vet[i] == 9
	
	if vet[i] == 7:
		vet[i] = 8
		
print(vet)