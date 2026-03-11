from numpy import *

nota = input().upper().split(",")
aux = zeros(5, dtype=int)

for i in range(size(nota)):
	if nota[i] == "A":
		aux[0] += 1
	elif nota[i] == "B":
		aux[1] += 1
	elif nota[i] == "C":
		aux[2] += 1
	elif nota[i] == "D":
		aux[3] += 1
	elif nota[i] == "E":
		aux[4] += 1
print(aux)