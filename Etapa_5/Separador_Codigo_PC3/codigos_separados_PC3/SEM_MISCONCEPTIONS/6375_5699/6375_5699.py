from numpy import *

vetor = input().split(",")

resultado = zeros(4,dtype=int)

for i in vetor:
	if i == "A":
		resultado[0] += 1
	elif i == "B":
		resultado[1] += 1
	elif i == "C":
		resultado[2] += 1
	else:
		resultado[3] += 1

print(resultado)