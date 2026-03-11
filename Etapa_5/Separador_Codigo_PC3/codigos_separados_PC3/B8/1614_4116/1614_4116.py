from numpy import *
from numpy.linalg import * 
from math import * 

alimentos = array(eval(input()))
for elemento in range(size(alimentos)):
	if elemento == "BANANA":
		elemento = 0.97
	elif elemento == "BIFE":
		elemento = 2.95
	elif elemento == "FEIJOADA":
		elemento = 1.27
	elif elemento == "OMELETE":
		elemento = 1.04
	elif elemento == "TOMATE":
		elemento = 0.2

alimentos = zeros(elemento, dtype=int)
quantidade = array(eval(input()))
quantidade = quantidade.T

t = dot(inv(alimentos), quantidade)

print(round(t, 0))