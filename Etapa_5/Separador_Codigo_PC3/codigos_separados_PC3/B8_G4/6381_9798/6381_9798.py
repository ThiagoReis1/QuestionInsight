from numpy import *
x = array(input("Insira: ").upper().split(","))
cont = zeros(4, dtype=int)
for i in range(size(x)):
	if x[i] == "C":
		cont[0] = cont[0] + 1
	elif x[i] == "O":
		cont[1] = cont[1] + 1
	elif x[i] == "P":
		cont[2] = cont[2] + 1
	elif x[i] == "E":
		cont[3] = cont[3] + 1
print(cont)