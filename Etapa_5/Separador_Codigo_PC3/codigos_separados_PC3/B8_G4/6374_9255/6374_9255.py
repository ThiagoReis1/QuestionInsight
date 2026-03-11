from numpy import *
pat = input("Tipo de paciente: ").upper().split(",")

cont = zeros(4, dtype = int)

for i in range(size(pat)):
	if pat[i] == "O":
		cont[0] = cont[0] + 1
	elif pat[i] == "D":
		cont[1] = cont[1] + 1
	elif pat[i] == "N":
		cont[2] = cont[2] + 1
	elif pat[i] == "C":
		cont[3] = cont[3] + 1
	
print(cont)


