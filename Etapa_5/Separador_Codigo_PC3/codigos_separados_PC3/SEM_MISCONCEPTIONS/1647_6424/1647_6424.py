from numpy import *
v = array(eval(input()))
c = -1
a = 0
lista = []
for i in range(size(v)):
	if v[i] >= 70:
		a += 1
for x in range(size(v)):
	c += 1
	if v[x] >= 70:
		lista.append(c)
		vetor = array(lista)
print(a)
print(vetor)