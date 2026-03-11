from numpy import *

nota = input("Notas: ").upper().split(',')
nota2 = zeros(5, dtype=int)
for v in nota:
	if v == 'A':
		nota2[0] += 1
	elif v == 'B':
		nota2[1]+= 1
	elif v == 'C':
		nota2[2] += 1
	elif v == 'D':
		nota2[3] += 1
	elif v == 'E':
		nota2[4] += 1
print(nota2)