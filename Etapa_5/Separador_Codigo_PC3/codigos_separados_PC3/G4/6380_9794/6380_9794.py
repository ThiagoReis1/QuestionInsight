from numpy import *
s = input("Insira o produto: ").upper().split(",")
cont = zeros(4, dtype=int)
for i in s:
	if i == "E":
		cont[0] = cont[0] + 1
	if i == "V":
		cont[1] = cont[1] + 1
	if i == "A":
		cont[2] = cont[2] + 1
	if i == "D":
		cont[3] = cont[3] + 1
print(cont)
			