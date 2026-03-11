from numpy import*

vet = input("").upper()

cont = zeros(4, dtype= int)

for i in range(len(vet)):
	if vet[i] == "O":
		cont[0] += 1
	elif vet[i] == "D":
		cont[1] += 1
	elif vet[i] == "N":
		cont[2] += 1
	elif vet[i] == "C":
		cont[3] += 1
print(cont)