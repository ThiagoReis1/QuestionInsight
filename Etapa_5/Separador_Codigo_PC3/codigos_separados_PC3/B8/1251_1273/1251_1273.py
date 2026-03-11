from numpy import *

vector = array(eval(input("Entre com o vetor: ")))

A = min(vector)
B = max(vector)

C = 0.7 * A + 0.3 * B

D = 0.4 * A + 0.6 * B

resultado = zeros(2, dtype = int)

for x in vector:
	if (C <= x < D):
		resultado[0] = resultado[0] + 1
	elif(D <= x < B):
		resultado[1] = resultado[1] + 1

print(resultado)
		