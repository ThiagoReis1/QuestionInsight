from numpy import*
cont = zeros(5, dtype=int)
vet = input("Insira dado:").upper().split(',')

for i in range(size(vet)):
	if(vet[i] == "P"):
		cont[0] = cont[0]+1
	elif(vet[i] == "C"):
		cont[1] = cont[1]+1
	elif(vet[i] == "R"):
		cont[2] = cont[2]+1
	elif(vet[i] == "L"):
		cont[3] = cont[3]+1
	elif(vet[i] == "B"):
		cont[4] = cont[4]+1

print(max(cont))
print(cont)