from numpy import *
tons = input("tons de pele: ").split(',')
cont = 0
zeros = zeros(5, dtype=int)
for i in range(size(tons)):
	if tons[i] == "MC":
		cont[0] = cont[0] + 1
	elif tons[i] == "C":
		cont[1] = cont[1] + 1
	elif tons[i] == "CM":
		cont[2] = cont[2] + 1
	elif tons[i] == "EM":
		cont[3] = cont[3] + 1
	elif tons[i] == "E":
		cont[4] = cont[4] + 1
	elif tons[i] == "ME":
		cont[5] = cont[5] + 1
print(cont)