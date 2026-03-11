# Importar o módulo de vetor
from numpy import *
from math import *

# Leitura do vetor
v = array(eval(input("Digite um vetor: ")))

s = 0 # variável contadora
for i in range(size(v)):
	s = s + log(v[i] + 1)

m = exp(s/size(v)) - 1

print(round(m,2))