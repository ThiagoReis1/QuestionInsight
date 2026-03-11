# Importar o módulo de vetor
from numpy import *

# Leitura do vetor
v = array(eval(input("Digite o vetor: ")))

i = 0 # Variável contadora
s = ones(size(v),dtype=float)

while i < size(v):
	if v[i] > 8:
		s[i]= 10
		i=i+1
	elif v[i] < 2:
		s[i]=0
		i=i+1
	else:
		s[i]=v[i]
		i=i+1
		
print(s)