from numpy import *

projs = []

for i in range(10):
	entrada = int(input())
	projs.append(entrada)
	

minimo = int(input())
aprovados = []

for i in projs:
	if i >= minimo:
		aprovados.append(i)
		
print(array(aprovados))