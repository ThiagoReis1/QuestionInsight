from numpy import *

vet = input("")

cus = 0
i = 0

while (i < len(vet)):
	if ((vet[i] == "A") or (vet[i] == "E") or (vet[i] == "I") or (vet[i] == "O") or (vet[i] == "U")):
		cus = cus + 25.12
		i += 1
	else:
		cus = cus + 40.18
		i += 1
		
print(round(cus, 2))