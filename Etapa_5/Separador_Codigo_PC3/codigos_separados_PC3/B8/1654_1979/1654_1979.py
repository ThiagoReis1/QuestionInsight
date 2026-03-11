from numpy import*

estados = input("Insira o vetor de estados:\n").upper().split(',')

cont = zeros(5, dtype = int)

for i in range(len(estados)):
	if(estados[i] == "AM"):
		cont[0] = cont[0] + 1
	elif(estados[i]) == "PE":
		cont[1] = cont[1] + 1
	elif(estados[i] == "MG"):
		cont[2] = cont[2] + 1
	elif(estados[i] == "SP"):
		cont[3] = cont[3] + 1
	elif(estados[i] == "RS"):
		cont[4] = cont[4] + 1
print(max(cont))
print(cont)