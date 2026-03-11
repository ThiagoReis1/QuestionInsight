from numpy import*

vet = input(" insira a tarefa: ").upper().split(",")
cont = zeros(4, dtype=int)
i = 0

for j in range(size(vet)):
	if vet[j] == "A":
		cont[0] = cont[0] + 1
	elif vet[j] == "P": 
		cont[1] = cont[1] + 1
	elif vet[j] == "D":
		cont[2] = cont[2] + 1
	elif vet[j] == "M": 
		cont[3] = cont[3] + 1
	i = i + 1
print(cont)