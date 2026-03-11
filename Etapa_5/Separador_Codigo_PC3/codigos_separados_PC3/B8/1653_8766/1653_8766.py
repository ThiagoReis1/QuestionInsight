from numpy import *
vet =input("Digitea nacionalidade das pessoas:").upper().split(',')

cont = zeros(5,dtype = int)

for i in range(len(vet)):
	if vet[i] == "AR":
		cont[0] = cont[0] + 1
	elif vet[i] == "BR":
		cont[1] = cont[1] + 1
	elif vet[i] == "CL":
		cont[2] = cont[2] + 1
	elif vet[i] == "CO":
		cont[3] = cont[3] + 1
	elif vet[i] == "UY":
		cont[4] = cont[4] + 1
string = array(cont)
print(max(string))
print(cont)
	
	