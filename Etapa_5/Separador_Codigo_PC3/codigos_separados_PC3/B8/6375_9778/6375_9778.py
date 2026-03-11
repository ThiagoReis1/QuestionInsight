from numpy import *

cont = zeros (4, dtype=int)
candidato = input("").upper().split(",")

for v in candidato:
	if v == 'A':
		cont[0] += 1
	elif v == 'B':
		cont[1] += 1
	elif v == 'C':
		cont [2] += 1
	elif v == 'D':
		cont [3] += 1
print(cont)