from numpy import*
paciente = input(" ")
cont = zeros(4, dtype = int)

for i in range(len(paciente)):
	if(paciente[i] == "O"):
		cont[0] += 1
	if(paciente[i] == "D"):
		cont[1] += 1
	if(paciente[i] == "N"):
		cont[2] += 1
	if(paciente[i] == "C"):
		cont[3] += 1
print(cont)