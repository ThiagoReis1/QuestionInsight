# Talita Oliveira Gomes Passos
# 25 de Agosto de 2016
# Avaliação 6 - Ex 01

from numpy import *

v = array(eval(input("Digite um vetor: ")))

A = min(v)
B = max(v)

C = 0.75 * A + 0.25 * B
D = 0.25 * A + 0.75 * B

x = array(zeros(2, dtype = int))

for elemento in range(size(v)):
	i = 0
	if(v[i] >= C and v[i] < D):
		v[i] = i + 1
		x[0] = v[i]
		
		if(v[i] >= D and v[i] < B):
			v[i] = i + 1
			x[1] = v[i]
		
print(x)
	
	