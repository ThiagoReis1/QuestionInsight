from numpy import *

color = input(": ").split(",")
vet_cor = zeros(5, dtype=int)

for olhos in color:
	if olhos.upper() == "P":
		vet_cor[0] += 1
		
	elif olhos.upper() == "C":
		vet_cor[1] += 1
		
	elif olhos.upper() == "M":
		vet_cor[2] += 1
		
	elif olhos.upper() == "V":
		vet_cor[3] += 1
		
	else:
		vet_cor[4] += 1

print(max(vet_cor))
print(vet_cor)
