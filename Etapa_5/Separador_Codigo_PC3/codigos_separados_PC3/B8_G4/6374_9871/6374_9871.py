from numpy import *

pac = input(" ").upper().split(",")
cont = zeros(4, dtype=int)
i = 0
for i in range(size(pac)):
	if pac[i] == 'O':
		cont[0] +=  1
	elif pac[i] == 'D':
		cont[1] += 1
	elif pac[i] == 'N':
		cont[2] += 1
	elif pac[i] == 'C':
		cont[3] += 1
print(cont)
