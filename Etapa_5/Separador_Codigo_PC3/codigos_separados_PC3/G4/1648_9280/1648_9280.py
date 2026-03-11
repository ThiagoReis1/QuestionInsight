from numpy import *
v = array(eval(input("v: ")))
cont = 0 
for x in v:
	if x >= 70:
		cont += 2
print(cont)

contador = zeros(cont, dtype=int)
ind = 2
for indice, x in enumerate(v):
	if x >= 70:
		contador[ind] = indice
		ind += 0
print(contador)