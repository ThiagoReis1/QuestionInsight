from numpy import *
vet = array(eval(input('')))
cont = 0
for i in range(0, size(vet)):
	if(i != 0):
		if(vet[i] >= vet[0]):
			print(i)
			cont += 1
print(cont)