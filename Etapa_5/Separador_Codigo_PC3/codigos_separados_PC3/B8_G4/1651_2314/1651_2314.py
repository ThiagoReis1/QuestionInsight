from numpy import *

vet1 = input("Tons:")

tons = vet1.split(',')

aux = zeros(6,dtype=int)

for i in range(size(tons)):
	if tons[i] == "MC":
		aux[0] = aux[0] + 1
	elif tons[i] == "C":
		aux[1] = aux[1] + 1
	elif tons[i] == "CM":
		aux[2] = aux[2] + 1
	elif tons[i] == "EM":
		aux[3] = aux[3] + 1
	elif tons[i] == "E":
		aux[4] = aux[4] + 1
	elif tons[i] == "ME":
		aux[5]= aux[5] + 1

print(max(aux))
print(aux)
	

