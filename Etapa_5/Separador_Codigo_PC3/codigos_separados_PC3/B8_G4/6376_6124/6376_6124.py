from numpy import*

cont = zeros(4, dtype=int)
vet = input("Notas: ").upper().split(",")
for i in range(size(vet)):
	if (vet[i] == "A"):
		cont[0] = cont[0] + 1 
	elif (vet[i] == "B"):
		cont[1] = cont[1] + 1        
	elif (vet[i] == "C"):
		cont[2] = cont[2] + 1
	elif (vet[i] == "D"):
		cont[3] = cont[3] + 1
print(cont)