# Universidade Federal do Amazonas
# Introduao a ciencia dos computadores
# Avaliacao 5 - 21552438

from math import* 
from numpy import* 
v = array(eval(input("Digite o vetor: ")))

den = size(v) - 1 
x = 0 
for i in range(size(v)):
	x = x + (v[i] - m) ** 2 
print(round(sqrt(x/den), 7))

