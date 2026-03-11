from numpy import *

caractere = input().upper().split(',')

cont = zeros(4, dtype=int)

for x in caractere:
	if x == "A":
		cont[0] += 1
	elif x == "B":
		cont[1] += 1
	elif x == "C":
		cont[2] += 1
	elif x == "D":
		cont[3] += 1
		
	
print(cont)