from numpy import *

pais = input("nacionalidade das pessoas: ").upper().split(',')

vet_cont = zeros(5, dtype = int)

for i in range(size(pais)):
	if pais[i] == "AR":
		vet_cont[0] += 1
	elif pais[i] == "BR":
		vet_cont[1] += 1
	elif pais[i] == "CL":
		vet_cont[2] += 1
	elif pais[i] == "CO":
		vet_cont[3] += 1
	elif pais[i] == "UY":
		vet_cont[4] += 1
print(max(vet_cont))
print(vet_cont)