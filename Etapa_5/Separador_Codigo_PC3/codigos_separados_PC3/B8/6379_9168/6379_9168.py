from numpy import *

notas = input("Escreva a sequencia de caracteres: ").upper()
classe = zeros(5, dtype = int)

for i in range(len(notas)):
	if notas[i] == "A":
		classe[0] += 1
	elif notas[i] == "B":
		classe[1] += 1
	elif notas[i] == "C":
		classe[2] += 1
	elif notas[i] == "D":
		classe[3] += 1
	elif notas[i] == "E":
		classe[4] += 1
print(classe)

