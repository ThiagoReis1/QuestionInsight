from numpy import *

notas = input().upper().split(',')
cont = zeros(4, dtype=int)

for v in notas:
	if v == "C":
		cont[0] += 1
	elif v == "D":
		cont[1] += 1
	elif v == "V":
		cont[2] += 1
	elif v == "U":
		cont[3] += 1
		
print(cont)