# Importar o módulo de vetor
from numpy import *

# Leitura do vetor
v = array(eval(input("Digite um vetor: ")))

for i in range(size(v)):
	if v[i] == 0:
		v[i] = 9
	else:
		v[i] = v[i] - 1
		
print(v)		