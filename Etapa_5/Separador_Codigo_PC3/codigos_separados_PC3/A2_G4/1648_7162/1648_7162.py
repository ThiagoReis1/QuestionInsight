# Importar módulo de vetor
from numpy import *

# Leitura do vetor
v = array(eval(input("Digite um vetor: ")))

r = 0 # variável contadora

for i in range(size(v)):
	if v[i] < 70:
		r = r + 1
	else:
		r = r
print(r)

z = zeros(r, dtype = int)
j = 0 # posição
for i in range(size(v)):
	if v[i] < 70:
		z[j] = i
		j = j+1

print(z)		