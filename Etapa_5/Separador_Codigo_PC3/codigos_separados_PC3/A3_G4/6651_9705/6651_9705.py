from numpy import *

notas = array(eval(input()))
n1 = notas[0] * 5
n2 = notas[1] * 4
n3 = notas[2] * 3
n4 = notas[3] * 2
i = 0
nota_final = 0

while i < len(notas):
	nota_final = (n1 + n2 + n3 + n4)/14
	i += 1
print(round(nota_final, 2))
	