from numpy import *
v = array(eval(input("v: ")))
cont = 0
for x in v:
	if x % 5 == 0:
		cont += 1
print(cont)
contador = zeros(cont, dtype=int)
c = 0
for indice, x in enumerate(v):
	if x % 5 == 0:
		contador[c] = indice
		c += 1
print(contador)