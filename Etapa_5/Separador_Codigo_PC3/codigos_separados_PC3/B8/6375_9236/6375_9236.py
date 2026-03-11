from numpy import*
candidato = input("digite o candidato: ").upper()
cont = zeros(4, dtype = int)

for i in range(len(candidato)):
	if (candidato[i] == "A"):
		cont[0] += 1
	elif(candidato[i] == "B"):
		cont[1] += 1
	elif(candidato[i] == "C"):
		cont[2] += 1
	elif(candidato[i] == "D"):
		cont[3] += 1
print(cont)