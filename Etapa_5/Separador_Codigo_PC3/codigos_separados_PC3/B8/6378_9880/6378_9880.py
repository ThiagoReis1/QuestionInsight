from numpy import *

notas = input("Insira o valor das notas: ").upper().split(",")

cont = zeros(4, dtype=int)

for i in notas:
	if i == "C":
		cont[0] +=1
	elif i == "D":
		cont[1] += 1
	elif i == "V":
		cont[2] += 1
	elif i == "U":
		cont[3] += 1

print(cont)