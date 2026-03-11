from numpy import *

saques= array(eval(input("saques: ")))
abaixo = 0

for i in range(size(saques)):
	if saques[i] <= 50:
		abaixo += 1
		
indice = zeros(abaixo, dtype=int)
print(abaixo)
j = 0

for i in range(size(saques)):
	if saques[i] <= 50:
		indice[j] = i
		j += 1
print(indice)