from numpy import*
vet = input("estados: ").split(',')
cont = zeros(5, dtype = int)
i = 0

for i in range(len(vet)):
	if (vet[i] == "AM"):
		cont[0] = cont[0] + 1
	elif (vet[i] == "PE"):
		cont[1] = cont[1] + 1
	elif (vet[i] == "MG"):
		cont[2] = cont[2] + 1
	elif (vet[i] == "SP"):
		cont[3] = cont[3] + 1
	elif (vet[i] == "RS"):
		cont[4] = cont[4] + 1
	
print(max(cont)) 
print(cont)	
