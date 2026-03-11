from numpy import*
vet=input(": ").upper().split(',')
cont = zeros(5, dtype = int)
for x in range(size(vet)):
	if(vet[x]=='AC'):
		cont[0] = cont[0] + 1
	elif(vet[x]=='AM'):
		cont[1] = cont[1] + 1
	elif(vet[x]=='PA'):
		cont[2] = cont[2] + 1
	elif(vet[x]=='RO'):
		cont[3] = cont[3] + 1
	elif(vet[x]=='RR'):
		cont[4] = cont[4] + 1

print(max(cont))
print(cont)
	
	