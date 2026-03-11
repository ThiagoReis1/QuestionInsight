from numpy import *

v = input("Escreva uma das letras: ").upper().split(",")

v1 = zeros(4, dtype=int)

for i in range(len(v)):
	if v[i] == "A":
		v1[0] += 1
	elif v[i] == "B":
		v1[1] += 1
	elif v[i] == "C":
		v1[2] += 1
	elif v[i] == "D":
		v1[3] += 1
		
print(v1)