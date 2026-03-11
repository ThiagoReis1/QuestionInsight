from numpy import *
n = input("Caractere da carta: ").upper().split(",")

cont = zeros(4, dtype = int)

for d in range(size(n)):
	if n[d] == 'C':
		cont[0] += 1
	elif n[d] == 'O':
		cont[1] += 1
	elif n[d] == 'P':
		cont[2] += 1
	elif n[d] == 'E':
		cont[3] += 1
print(cont)
