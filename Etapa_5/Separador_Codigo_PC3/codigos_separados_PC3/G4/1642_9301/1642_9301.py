from numpy import *
v = array(eval(input("digite o vetor: ")))
cont = 0
for x in v:
	if x % 5 == 0:
		cont += 1
print(cont)
contador = zeros(cont, dtype=int)
ind = 0
for indice, x in enumerate(v):
	if x % 5 == 0:
		contador[ind] = indice
		ind += 1
print(contador)
