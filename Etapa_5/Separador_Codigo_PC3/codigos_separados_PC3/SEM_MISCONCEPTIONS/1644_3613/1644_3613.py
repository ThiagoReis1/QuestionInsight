from numpy import *

notas = array(eval(input()))
cont =0
for i in notas:
	if i <5:
		cont+=1
print(cont)
posi = zeros(cont, dtype=int)
cont = 0
for i in range(size(notas)):
	if notas[i]<5:
		posi[cont] = i
		cont+=1

print(posi)