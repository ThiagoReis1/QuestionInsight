from numpy import*
vet = input("pais: ").upper().split(",")
cont = zeros(5, dtype = int)
for x in range(size(vet)):
	if(vet[x] == "CHN"):
		cont[0] = cont[0] + 1
	elif(vet[x] == "JPN"):
		cont[1] = cont[1] + 1
	elif(vet[x] == "KOR"):
		cont[2] = cont[2] + 1
	elif(vet[x] == "MGL"):
		cont[3] = cont[3] + 1
	elif(vet[x] == "THA"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)