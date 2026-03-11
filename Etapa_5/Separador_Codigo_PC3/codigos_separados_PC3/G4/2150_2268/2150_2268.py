from numpy import *
vet = array(eval(input("vet: ")))
cont = zeros(4, dtype=int)
for x in range(size(vet)):
	if(vet[x] == "BOTAFOGO"):
		cont[0] = cont[0] + 1
	if(vet[x] == "FLAMENGO"):
		cont[1] = cont[1] + 1
	if(vet[x] == "FLUMINENSE"):
		cont[2] = cont[2] + 1
	if(vet[x] == "VASCO"):
		cont[3] = cont[3] + 1
print(cont)

	