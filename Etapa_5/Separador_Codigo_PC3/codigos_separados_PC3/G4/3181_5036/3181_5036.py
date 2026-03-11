from numpy import *

v = array(eval(input('jogadas: ')))

vet = zeros(37, dtype=int)

for x in v:
	for i in range(37):
		if x == i:
			vet[i] += 1
			
print(vet)