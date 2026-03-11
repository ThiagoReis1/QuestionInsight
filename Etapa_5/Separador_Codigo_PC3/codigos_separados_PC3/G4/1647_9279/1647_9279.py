from numpy import *
v = array(eval(input("v: ")))
cont = 0
for x in v:
	if x >= 70:
		cont += 1
print(cont)
contador = zeros(cont, dtype=int)
ind = 0
for indice, x in enumerate(v):
	if x >= 70:
		contador[ind] = indice
		ind += 1
print(contador)	