import numpy as np

vet = input()
total = contD = contS = contI = i = 0

while i < len(vet):
	if vet[i] == 'D':
		total = total + 2.25
		contD = contD +1
	elif vet[i] == 'S':
		total = total + 4.00
		contS = contS + 1
	else:
		total = total + 6.90
		contI = contI + 1
	i = i + 1
	
print(round(total, 2), contD, contS, contI)
	