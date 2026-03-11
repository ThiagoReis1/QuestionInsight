from numpy import *

let = input("Generos: ").upper().split(",")

cont = zeros(4,dtype = int)

for i in range(size(let)):
	if let[i] == "C":
		cont[0] = cont[0] + 1
	elif let[i] == "O":
		cont[1] = cont[1] + 1
	elif let[i] == "P":
		cont[2] = cont[2] + 1
	elif let[i] == "E":
		cont[3] = cont[3] + 1
print(cont)
