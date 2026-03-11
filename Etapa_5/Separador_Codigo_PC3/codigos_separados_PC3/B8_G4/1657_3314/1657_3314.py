from numpy import *

vet=input("Digite a string: ").split(",")
cont = zeros(5,dtype=int)
for i in range(size(vet)):
	if (vet[i] == "AZ"):
		cont[0] = cont[0] + 1 
	elif (vet[i] == "CA"):
		cont[1] = cont[1] + 1 
	elif (vet[i] == "FL"):
		cont[2] = cont[2] + 1
	elif (vet[i] == "PA"):
		cont[3] = cont[3] + 1
	elif (vet[i] == "WI"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)