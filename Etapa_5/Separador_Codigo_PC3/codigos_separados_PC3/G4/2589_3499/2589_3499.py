from numpy import *
vet = array(eval(input("")))
cont = 0
for i in range(size(vet)):
	if(vet[0] != 0):
		if(vet[i] >= vet[0]):
			print(i)
			cont += 1		
print(cont)
